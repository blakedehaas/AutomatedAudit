---

# Automated Audit Tool

## Overview

The Automated Audit Tool is designed to automate the process of auditing multiple repositories for specified terms and generating audit reports in Word documents. This tool leverages Python and utilizes configurations set in `config.py` to perform the audit.

## Features

- **Configuration-driven**: Read configurations from `config.py` to specify repositories, terms to audit, document generation settings, and grep command templates.
  
- **Repository Auditing**: Iterates over a list of repositories specified in `config.py` and performs a grep command for each term.
  
- **Document Generation**: Generates a separate Word document for each audited repository containing detailed audit results.

## Prerequisites

Before using the tool, ensure:
- You have Python installed (Python 3.6 or higher).
- Required Python packages (`pandas`, `python-docx`) are installed (`pip install pandas python-docx`).

## Usage

1. **Configuration Setup**:
   - Edit `config.py` to configure the list of terms (`terms`), repository directory (`repositoryDirectory`), document folder (`documentFolder`), document heading template (`documentHeadingTemplate`), default action (`defaultAction`), and default justification (`defaultJustification`).

2. **Clone Repositories**:
   - Clone the repositories you want to audit into the directory specified by `repositoryDirectory` in `config.py`.

3. **Run the Script**:
   - Execute `automate_audit.py`.
   - The script will iterate over each repository, grep for each term, collect results, and generate corresponding Word documents in the specified `documentFolder`.

4. **Review Audit Results**:
   - Each generated Word document will contain a summary of audit results for the respective repository.

## File Descriptions

- **`automate_audit.py`**: Main script that performs the audit based on configurations in `config.py`, utilizes `pandas` for data handling, and `python-docx` for Word document generation.
  
- **`config.py`**: Configuration file where terms, repositories, document settings, and grep command templates are defined.

## Notes

- Ensure repositories are correctly cloned and paths are configured in `config.py` before running the script.
- Document generation relies on Python's `python-docx` library for Word document manipulation.

## Attributions
- This tool was created with coding assistance from ChatGPT

---