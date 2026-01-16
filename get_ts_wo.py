import os

# -----------------------------
# CONFIGURATION
# -----------------------------

BASE_DIR = r"C:\PATH\TO\ROOT\FOLDER"

INTERNAL_REVIEW_DIR = os.path.join(BASE_DIR, "INTERNAL_REVIEW")
COMPLETE_DIR = os.path.join(BASE_DIR, "COMPLETE")

INPUT_FILE = "enter_jobs_here.txt"
OUTPUT_FILE = "WO_list.txt"
NOTES_FILENAME = "structural_notes.txt"

# -----------------------------
# LOAD JOB IDS
# -----------------------------

with open(INPUT_FILE, "r") as f:
    entered_jobs = [line.strip() for line in f if line.strip()]

# -----------------------------
# LOAD FOLDER LISTS
# -----------------------------

internal_review_folders = set(os.listdir(INTERNAL_REVIEW_DIR))
complete_folders = set(os.listdir(COMPLETE_DIR))

# -----------------------------
# PROCESS JOBS
# -----------------------------

with open(OUTPUT_FILE, "w") as wo_list:

    for job_id in entered_jobs:
        job_path = None

        if job_id in internal_review_folders:
            job_path = os.path.join(INTERNAL_REVIEW_DIR, job_id)

        elif job_id in complete_folders:
            job_path = os.path.join(COMPLETE_DIR, job_id)

        if not job_path:
            wo_list.write(f"Job ID: {job_id} / WO: NOT FOUND\n")
            continue

        notes_path = os.path.join(job_path, NOTES_FILENAME)

        if not os.path.exists(notes_path):
            wo_list.write(f"Job ID: {job_id} / WO: FILE NOT FOUND\n")
            continue

        with open(notes_path, "r", encoding="utf-8", errors="ignore") as job_file:
            for line in job_file:
                if line.startswith("WO#: "):
                    wo = line.replace("WO#: ", "").strip()
                    wo_list.write(f"Job ID: {job_id} / WO: {wo}\n")
                    break
            else:
                wo_list.write(f"Job ID: {job_id} / WO: NOT FOUND IN FILE\n")