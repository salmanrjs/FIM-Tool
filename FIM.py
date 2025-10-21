
import os
import pyfiglet
import hashlib  # Needed for calculating file hashes
import argparse  # Needed for handling command-line arguments (like --init, --check)
import json  # Needed for saving and loading the baseline file
import colorama  # Needed for terminal colors
from colorama import Fore, Style

#  Colors
colorama.init(autoreset=True)

# --- Settings ---
BANNER_TEXT = "F     I     M"  # Banner text with spaces as requested
BASELINE_FILE = 'baseline.json'  # Our database file to store hashes


def print_banner():

    banner = pyfiglet.figlet_format(BANNER_TEXT)

    print(Fore.RED + banner)

    # Print tool information
    print(Style.BRIGHT + "======================================================")
    print(Style.BRIGHT + "      File Integrity Monitor (FIM) v0.1")
    print(Style.BRIGHT + "      Developed by: [Salman Rajab]")
    print(Style.BRIGHT + "======================================================")
    print("\n")


def calculate_hash(filepath):

    sha256_hash = hashlib.sha256()  # Create a new SHA-256 hash object
    try:
        # Open the file in binary read mode ('rb')
        with open(filepath, "rb") as f:

            while chunk := f.read(65536):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()  # Get the final hash string

    except IOError as e:

        print(Fore.YELLOW + f"  [!] Skipping {filepath} (Permission Error: {e.filename})")
        return None
    except Exception as e:
        print(Fore.YELLOW + f"  [!] Skipping {filepath} (Error: {e})")
        return None


def initialize_baseline(target_directory):

    baseline = {}  # Create an empty dictionary to store hashes
    file_count = 0
    print(Fore.CYAN + f"[*] Scanning files in {target_directory}...")


    for root, dirs, files in os.walk(target_directory):
        for file in files:

            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)

            if file_hash:

                baseline[file_path] = file_hash
                file_count += 1
                print(f"  [+] Hashed: {file_path}")

    try:
        with open(BASELINE_FILE, 'w') as f:

            json.dump(baseline, f, indent=4)

        print("\n" + Fore.GREEN + Style.BRIGHT + "[SUCCESS] Baseline created!")
        print(Fore.GREEN + f"[*] Saved hashes for {file_count} files to {BASELINE_FILE}")

    except Exception as e:
        print("\n" + Fore.RED + Style.BRIGHT + f"[FATAL ERROR] Could not write baseline file!")
        print(Fore.RED + f"[*] Reason: {e}")


def check_integrity(target_directory):

    # 1 - Load the saved baseline
    try:
        with open(BASELINE_FILE, 'r') as f:
            # Load the hashes from the JSON file into a dictionary
            baseline = json.load(f)
        print(Fore.GREEN + f"[*] Successfully loaded baseline from {BASELINE_FILE}")
    except FileNotFoundError:
        print(Fore.RED + f"[!] Error: Baseline file '{BASELINE_FILE}' not found.")
        print(Fore.YELLOW + f"[*] Please run '--init {target_directory}' first.")
        return
    except Exception as e:
        print(Fore.RED + f"[!] Error loading baseline file: {e}")
        return

    # 2 - Scan the directory again to get current state
    print(Fore.CYAN + f"[*] Scanning current files in {target_directory}...")
    current_hashes = {}

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash:
                current_hashes[file_path] = file_hash

    # 3 - Compare current state with the baseline
    print("[*] Comparing current files against baseline...")

    baseline_files = set(baseline.keys())
    current_files = set(current_hashes.keys())

    # Files that are in the baseline but NOT on the disk now
    deleted_files = baseline_files - current_files
    # Files that are on the disk now but NOT in the baseline
    new_files = current_files - baseline_files
    # Files that are in both, we need to check their hashes
    common_files = baseline_files.intersection(current_files)

    modified_files = []
    for file_path in common_files:
        if baseline[file_path] != current_hashes[file_path]:

            modified_files.append(file_path)

    # 4 - Print the final report
    print("\n" + Style.BRIGHT + "--- [ Integrity Check Report ] ---")

    if not modified_files and not new_files and not deleted_files:
        print(Fore.GREEN + Style.BRIGHT + "\n[+] SUCCESS: All files are intact. No changes detected.")
        return

    if modified_files:
        print(Fore.RED + Style.BRIGHT + "\n[!] MODIFIED FILES (DANGER!):")
        for file_path in modified_files:
            print(f"  - {file_path}")

    if new_files:
        print(Fore.YELLOW + Style.BRIGHT + "\n[!] NEW FILES (SUSPICIOUS):")
        for file_path in new_files:
            print(f"  - {file_path}")

    if deleted_files:
        print(Fore.YELLOW + Style.BRIGHT + "\n[!] DELETED FILES (NOTICE):")
        for file_path in new_files:
            print(f"  - {file_path}")


def main():

    print_banner()

    parser = argparse.ArgumentParser(
        description="A simple File Integrity Monitor.",
        add_help=False  # Disable the default help
    )

    parser.add_argument('--init', metavar='DIR', help='Initialize a new baseline for a directory.')
    parser.add_argument('--check', metavar='DIR', help='Check a directory against the baseline.')


    args = parser.parse_args()

    # - Logic
    if args.init:
        target_directory = args.init
        if not os.path.isdir(target_directory):
            print(Fore.RED + f"[!] Error: Directory not found: {target_directory}")
            return
        print(f"[+] Starting baseline initialization for: {target_directory}")
        initialize_baseline(target_directory)

    elif args.check:
        target_directory = args.check
        if not os.path.isdir(target_directory):
            print(Fore.RED + f"[!] Error: Directory not found: {target_directory}")
            return
        print(f"[+] Starting integrity check for: {target_directory}")
        check_integrity(target_directory)

    # If no command is given, print our custom usage screen
    else:
        print(Fore.CYAN + Style.BRIGHT + "Usage: python fim.py [COMMAND] [DIRECTORY]")
        print("\n" + Style.BRIGHT + "Available Commands:")

        print(Fore.GREEN + "  --init   <DIR>" + Style.RESET_ALL + "       Initialize a new baseline for a directory.")
        print(Fore.GREEN + "  --check  <DIR>" + Style.RESET_ALL + "       Check a directory against the baseline.")


        print(Style.BRIGHT + "\nExamples:")
        print("  python fim.py --init ./important_files")
        print("  python fim.py --check ./important_files")


if __name__ == "__main__":
    main()