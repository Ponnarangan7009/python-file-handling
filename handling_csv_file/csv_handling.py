"""Reading, writing, and appending CSV test results."""

import csv
from pathlib import Path


# Anchor paths to this script, so they work from different current folders.
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_CSV = SCRIPT_DIR / "test_results.csv"
OUTPUT_CSV = SCRIPT_DIR / "generated_results.csv"
FIELDNAMES = ["test_name", "status", "duration_ms"]


# DictReader uses the first CSV row as the dictionary keys.
passed_count = 0
with open(INPUT_CSV, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        duration_ms = int(row["duration_ms"])
        print(f'{row["test_name"]}: {row["status"]}, {duration_ms} ms')

        if row["status"] == "PASS":
            passed_count += 1

print("Passed tests:", passed_count)


# Write a fresh CSV. Mode "w" replaces the output file if it already exists.
new_results = [
    {"test_name": "login", "status": "PASS", "duration_ms": 120},
    {"test_name": "payment", "status": "FAIL", "duration_ms": 350},
]

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(new_results)


# Append rows to an existing CSV. Do not write the header a second time.
additional_results = [
    {"test_name": "checkout", "status": "PASS", "duration_ms": 440},
    {"test_name": "Logout", "status": "FAIL", "duration_ms": 111},
]

with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
    writer.writerows(additional_results)


# CSV notes:
# - CSV values are read as strings; convert numeric columns when needed.
# - newline="" lets the csv module handle line endings correctly.
# - Use csv.reader for list-based rows or DictReader for header-based rows.
# - The csv module handles commas and quotes in quoted fields; do not split
#   CSV lines manually on commas.

