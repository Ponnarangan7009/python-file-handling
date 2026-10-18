"""Practice exercises for reading and writing plain text files."""

from pathlib import Path


DATA_FOLDER = Path(__file__).resolve().parent.parent
SAMPLE_PATH = DATA_FOLDER / "sample.txt"
OUTPUT_PATH = Path(__file__).resolve().parent / "practice_output.txt"


# Exercise 1: Read SAMPLE_PATH with read() and print the contents.
# Then explain why read() returns one string even when the file has many lines.


# Exercise 2: Read only the first two lines using readline(). Print them
# without their trailing newline characters. Try reading a third time and
# observe what happens to the file cursor.


# Exercise 3: Read SAMPLE_PATH with a for loop. Print each line without an
# extra blank line. Hint: print(line, end="") or line.rstrip("\n").


# Exercise 4: Count how many lines contain "PASS" and how many contain
# "FAIL". Print both totals. Do not hard-code the totals.


# Exercise 5: Write a short report to OUTPUT_PATH using mode "w" and write().
# Include a newline between lines. Read the report back and print it.
# Keep sample.txt unchanged.


# Exercise 6: Append one more line to OUTPUT_PATH using mode "a". Run the
# exercise twice and observe why append mode keeps adding another copy.


# Exercise 7: Use Path.exists(), is_file(), and parent.is_dir() on SAMPLE_PATH.
# Also print its name, suffix, and parent folder.


# Exercise 8: Try opening DATA_FOLDER / "missing.txt" in read mode. Catch
# FileNotFoundError and print a helpful message. Use a specific exception.


# Exercise 9: Compare Path.cwd() with Path(__file__).resolve().parent. Explain
# which folder each one represents and how that affects relative paths.
