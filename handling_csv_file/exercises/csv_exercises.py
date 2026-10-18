"""Practice exercises for reading and writing CSV test data.

Use test_results.csv in the parent folder as the input file.
"""

import csv
from pathlib import Path


DATA_FOLDER = Path(__file__).resolve().parent.parent
INPUT_CSV = DATA_FOLDER / "test_results.csv"


# Exercise 1: Read INPUT_CSV with csv.DictReader.
# - Print each test as: login: PASS, 120 ms
# - Convert duration_ms to int before using it as a number.
# - Count and print the number of PASS rows. The sample has 2 PASS rows.


# Exercise 2: Create pass_summary.csv in this exercises folder.
# Use csv.DictWriter with columns "status" and "count" and write a header.
# Write one row for the PASS count and one row for the FAIL count.
# Do not overwrite the input file.


# Exercise 3: Add a test name containing a comma, such as "search, filters",
# to a new row. Use csv.DictWriter and confirm it remains one CSV field.

