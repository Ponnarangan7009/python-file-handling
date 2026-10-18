# Python File Handling

Beginner lessons and practice for working with paths, text files, CSV, and JSON.

## Lessons

- `handling_txt_file/txt_handling.py` — reading and writing text, file modes,
  newlines, file cursors, `pathlib`, and handling a missing file.
- `python-pylib/pathlib_understanding.py` — current working directory, script
  folder, relative and absolute paths, folder creation, and path checks.
- `handling_csv_file/csv_handling.py` — reading, counting, writing, and
  appending CSV test results.
- `handling_json_file/json_handling.py` — loading, writing, updating, and
  validating JSON.

Each lesson area has an `exercises/` folder with prompts to practise the topic.
The text lesson includes `handling_txt_file/sample.txt` as its input file.

## Run the lessons

Run these from the project root:

```bash
python3 handling_txt_file/txt_handling.py
python3 python-pylib/pathlib_understanding.py
python3 handling_csv_file/csv_handling.py
python3 handling_json_file/json_handling.py
```

The lessons anchor their data paths to the script folder, so they can also be
launched while the current working directory is elsewhere. Generated demo
outputs are listed in `.gitignore`; the original sample files stay unchanged.

