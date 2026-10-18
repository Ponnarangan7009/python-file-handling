"""Read and write plain text files using open() and pathlib."""

from pathlib import Path


# Anchor file paths to this script's folder. A relative path passed to open()
# normally starts from the current working directory instead.
SCRIPT_DIR = Path(__file__).resolve().parent
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"
OUTPUT_PATH = SCRIPT_DIR / "generated_notes.txt"


# Read the entire file into one string.
with open(SAMPLE_PATH, "r", encoding="utf-8") as file:
    contents = file.read()
print("Whole file as one string:")
print(contents)


# readline() reads one line each time it is called. The newline is usually
# part of the returned string. The file cursor advances after each call.
with open(SAMPLE_PATH, "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
print("First line:", first_line.rstrip("\n"))
print("Second line:", second_line.rstrip("\n"))


# readlines() returns a list of lines. Iterating over the file reads lines
# one at a time and is usually a good choice for larger files.
with open(SAMPLE_PATH, "r", encoding="utf-8") as file:
    lines = file.readlines()
print("Lines as a list:", lines)

print("Read line by line:")
with open(SAMPLE_PATH, "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")  # Avoid adding a second newline.


# Mode "w" creates the file or replaces its existing contents.
# This writes to a separate output file so sample.txt remains unchanged.
with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
    file.write("Text file notes\n")
    file.write("write() writes a string.\n")
    file.writelines(["writelines() writes each string in an iterable.\n"])

# Mode "a" adds to the end. write() and writelines() do not add newlines
# automatically, so include \n where a line break is wanted.
with open(OUTPUT_PATH, "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")

print("Generated output:")
print(OUTPUT_PATH.read_text(encoding="utf-8"))


# pathlib also offers concise text-file methods.
backup_path = SCRIPT_DIR / "pathlib_demo.txt"
backup_path.write_text("Created with Path.write_text().\n", encoding="utf-8")
print("Path.read_text():", backup_path.read_text(encoding="utf-8"), end="")

# Path checks report the filesystem state, not what a suffix suggests.
print("Sample exists:", SAMPLE_PATH.exists())
print("Sample is a file:", SAMPLE_PATH.is_file())
print("Sample parent is a directory:", SAMPLE_PATH.parent.is_dir())

# seek(0) moves the cursor to the start of an open file; tell() reports the
# current cursor position. Text-mode positions are not simple character counts.
with open(SAMPLE_PATH, "r", encoding="utf-8") as file:
    print("Position at start:", file.tell())
    file.readline()
    print("Position after first line:", file.tell())
    file.seek(0)
    print("Position after seek(0):", file.tell())


# Catch the specific error expected if a file is missing.
missing_path = SCRIPT_DIR / "missing.txt"
try:
    with open(missing_path, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The requested file was not found.")


# Key reminders:
# - with closes the file even if an error occurs.
# - r reads, w replaces/creates, and a appends/creates.
# - read() returns one string; readlines() returns a list of strings.
# - .strip() removes whitespace at both ends; .rstrip("\n") removes only
#   trailing newline characters and preserves other spaces.
# - UTF-8 is a good explicit encoding for ordinary text files.
