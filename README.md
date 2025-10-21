# FIM - File Integrity Monitor

A simple, command-line File Integrity Monitor (FIM) built in Python. This tool scans a directory, creates a baseline of SHA-256 hashes, and detects any modifications, additions, or deletions to the files.

---

## Screenshots

*(Add your screenshots here)*

**Main Interface:**
![Main interface](link-to-screenshot-1.png)

**Detecting a Modified File:**
![Detecting a modified file](link-to-screenshot-2.png)

---

## Features

* **Create Baseline:** Securely store the "known good" state of your files.
* **Detect Changes:** Reports modified, new, or deleted files.
* **Cross-Platform:** Runs on both Windows and Kali Linux.

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/FIM-Tool.git](https://github.com/your-username/FIM-Tool.git)
    cd FIM-Tool
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

The tool has two modes: `--init` and `--check`.

### 1. Initialize Baseline (`--init`)

Use this command one time to create the `baseline.json` file for a directory.

```bash
python fim.py --init ./path/to/your/directory