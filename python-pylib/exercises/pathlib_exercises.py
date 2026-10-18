"""Practice exercises for pathlib paths, files, and folders."""

from pathlib import Path


SCRIPT_FOLDER = Path(__file__).resolve().parent
SAMPLE_FILE = SCRIPT_FOLDER.parent / "reports" / "daily" / "sample.txt"
PRACTICE_FOLDER = SCRIPT_FOLDER / "exercise_output" / "daily"


# Exercise 1: Print Path.cwd() and SCRIPT_FOLDER. Explain how they can differ.


# Exercise 2: Print the relative path to SAMPLE_FILE from the script folder,
# then print its absolute path. Check exists(), is_file(), and is_dir().


# Exercise 3: Create PRACTICE_FOLDER, including missing parents. Running the
# exercise a second time should not raise FileExistsError.


# Exercise 4: Create summary.txt inside PRACTICE_FOLDER using write_text().
# Then read it back with read_text() and print its contents.


# Exercise 5: Read SAMPLE_FILE one line at a time and print each line without
# its trailing newline. Use rstrip("\\n") to preserve other surrounding spaces.

