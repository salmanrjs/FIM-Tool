# FIM - File Integrity Monitor v1.0

A simple, command-line File Integrity Monitor (FIM) built in Python. This tool scans a directory, creates a baseline of SHA-256 hashes, and detects any modifications, additions, or deletions to the files.


## Features

* **Create Baseline:** Securely store the "known good" state of your files.
* **Detect Changes:** Reports modified, new, or deleted files.
* **Cross-Platform:** Runs on both Windows and Kali Linux.

---

## Installation

It is **highly recommended** to install the packages in a virtual environment (`venv`).
On **Kali Linux**, this is **required**.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/salmanrjs/FIM-Tool.git
    cd fim-Tool
    ```

2.  **Create and activate a virtual environment:**

    On Kali / Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required libraries:**
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

```


## Screenshots

<img width="543" height="400" alt="fim7" src="https://github.com/user-attachments/assets/e31ade0d-3030-4aa6-91ff-85cf5e774459" />

---

<img width="496" height="170" alt="fim3" src="https://github.com/user-attachments/assets/f7af3da9-ca2e-4527-9f55-5ece9b7fa8db" />

---











