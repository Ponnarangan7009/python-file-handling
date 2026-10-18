"""Working with current folders, absolute paths, and pathlib."""

from pathlib import Path


# The current working directory is where a relative path starts.
cwd = Path.cwd()
print("Current working directory:", cwd)

# The script's folder can differ from the current working directory.
script_folder = Path(__file__).resolve().parent
print("Folder containing this script:", script_folder)

# This relative path is interpreted from script_folder below.
relative_path = Path("reports") / "daily" / "sample.txt"
sample_path = script_folder / relative_path
absolute_path = sample_path.resolve()

print("Relative path from script folder:", relative_path)
print("Absolute path:", absolute_path)

# cwd / relative_path would instead resolve from the process's current folder.
# __file__ is useful when the script may be launched from another folder.


# Create nested folders beside this script.
# parents=True creates missing parent folders; exist_ok=True prevents an
# error when the final folder already exists.
reports_folder = script_folder / "reports"
daily_folder = reports_folder / "daily"
daily_folder.mkdir(parents=True, exist_ok=True)


# These methods inspect what actually exists at a path. The extension alone
# does not determine whether the path points to a file or directory.
print("Exists:", sample_path.exists())
print("Is file:", sample_path.is_file())
print("Is directory:", sample_path.is_dir())

if sample_path.is_file():
    print("Sample contents:")
    print(sample_path.read_text(encoding="utf-8"))


# Useful Path properties include .name, .suffix, and .parent.
print("Name:", sample_path.name)
print("Suffix:", sample_path.suffix)
print("Parent folder:", sample_path.parent)

