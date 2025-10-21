# FIM - File Integrity Monitor

A simple, command-line File Integrity Monitor (FIM) built in Python. This tool scans a directory, creates a baseline of SHA-256 hashes, and detects any modifications, additions, or deletions to the files.

---

## Screenshots

*(Add your screenshots here)*

**Main Interface:**
![Main interface] <img width="544" height="409" alt="Fim1" src="https://github.com/user-attachments/assets/64ea084d-9cbf-4197-a7d0-9613a3e6529f" />

**Detecting a Modified File:**
![Detecting a modified file] <img width="496" height="170" alt="fim3" src="https://github.com/user-attachments/assets/f7af3da9-ca2e-4527-9f55-5ece9b7fa8db" />

---

## Features

* **Create Baseline:** Securely store the "known good" state of your files.
* **Detect Changes:** Reports modified, new, or deleted files.
* **Cross-Platform:** Runs on both Windows and Kali Linux.

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/salmanrjs/FIM-Tool
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



