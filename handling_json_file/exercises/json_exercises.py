"""Practice exercises for reading and writing JSON data."""

import json
from pathlib import Path


DATA_FOLDER = Path(__file__).resolve().parent.parent
CONFIG_PATH = DATA_FOLDER / "config.json"
RESULT_PATH = DATA_FOLDER / "result.json"


# Exercise 1: Load config.json with json.load.
# Print base_url, browser, timeout, and the Python type of timeout.


# Exercise 2: Load result.json, change duration_ms to 200, and write the
# updated object to updated_result.json using json.dump(..., indent=4).
# Keep result.json unchanged as the original sample.


# Exercise 3: Use json.dumps to convert a Python dictionary to a JSON string.
# Then use json.loads to convert that string back into a Python object.


# Exercise 4: Catch json.JSONDecodeError when parsing malformed JSON text.
# Hint: json.loads('{"status": PASS}') is malformed because PASS needs quotes.

