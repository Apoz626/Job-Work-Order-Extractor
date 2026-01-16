JOB WORK ORDER EXTRACTOR
=======================

OVERVIEW
--------
The Job Work Order Extractor is a Python automation script that searches job folders
across multiple directories, extracts associated Work Order (WO) numbers from text
files, and compiles the results into a single output file.

This tool is designed to eliminate repetitive manual searching and copying when
working with large sets of job folders stored on a local file system.

--------------------------------------------------------------------

FEATURES
--------
- Reads job IDs from a text file
- Searches multiple directories for matching job folders
- Opens a notes file within each job folder
- Extracts Work Order numbers
- Outputs all results to a single text file
- Gracefully handles missing jobs or files

--------------------------------------------------------------------

PROJECT STRUCTURE
-----------------
job_automation/
│
├── get_ts_wo.py
├── enter_jobs_here.txt
├── WO_list.txt
├── run.bat (optional)
└── README.txt

--------------------------------------------------------------------

REQUIREMENTS
------------
- Python 3.x
- Windows operating system (paths can be adapted for macOS/Linux)
- No third-party libraries required

--------------------------------------------------------------------

SETUP
-----

1) CLONE OR DOWNLOAD
Clone the repository using Git, or download and extract the ZIP file.

2) CONFIGURE FOLDER PATHS
Open main.py and update the configuration section:

BASE_DIR = "C:\\PATH\\TO\\ROOT\\FOLDER"

This directory should contain the folders where job IDs are stored.

Example directory structure:

ROOT_FOLDER
│
├── INTERNAL_REVIEW
│   ├── 348594
│   │   └── structural_notes.txt
│
├── COMPLETE
│   ├── 348595
│   │   └── structural_notes.txt

3) PREPARE INPUT FILE
Edit enter_jobs_here.txt and add one job ID per line:

348594
348595
348600

--------------------------------------------------------------------

RUNNING THE SCRIPT
------------------

OPTION 1: FROM TERMINAL
Open a terminal in the project directory and run:

python main.py

OPTION 2: USING A BATCH FILE (WINDOWS)
Create a file called run.bat with the following contents:

@echo off
python main.py
pause

Double-click run.bat to execute the script.

--------------------------------------------------------------------

OUTPUT
------
After execution, the script creates or updates the file:

WO_list.txt

Output format:

Job ID: 348594 / WO: 1234893833
Job ID: 348595 / WO: 1234893840
Job ID: 348600 / WO: NOT FOUND

--------------------------------------------------------------------

ERROR HANDLING
--------------
The script safely handles:
- Job folders not found
- Missing notes files
- Work Order entries not present in files

The script does not delete or modify any existing files.

--------------------------------------------------------------------

DESIGN DECISIONS
----------------
- Centralized configuration for easy customization
- Defensive file handling to prevent crashes
- No external dependencies to support locked-down systems
- Designed for simple execution via terminal or batch file

--------------------------------------------------------------------

POSSIBLE IMPROVEMENTS
---------------------
- Read configuration from a config or JSON file
- Support multiple notes files per job
- Export results to CSV or Excel
- Add logging instead of console output
- Add automated tests

--------------------------------------------------------------------

PURPOSE
-------
This project demonstrates practical Python automation skills, including:
- File system navigation
- Text file parsing
- Defensive programming
- Workflow automation

It reflects common internal tooling used in real-world business environments.

--------------------------------------------------------------------

LICENSE
-------
This project is provided for educational and demonstration purposes.
