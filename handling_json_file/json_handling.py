"""Load, update, and write JSON data without replacing the sample input."""

import json
from pathlib import Path


# Anchor paths to this script so it also works when launched elsewhere.
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "config.json"
RESULT_PATH = SCRIPT_DIR / "result.json"
UPDATED_RESULT_PATH = SCRIPT_DIR / "updated_result.json"


# json.load() reads JSON text from a file and returns Python values.
with open(CONFIG_PATH, "r", encoding="utf-8") as file:
    config = json.load(file)

print("Base URL:", config["base_url"])
print("Timeout:", config["timeout"])
print("Timeout type:", type(config["timeout"]).__name__)
print("Browser:", config["browser"])

# JSON values map to Python values:
# object -> dict, array -> list, string -> str, number -> int or float,
# true/false -> True/False, null -> None.


# Load a result, update it, and write a separate output file. This preserves
# result.json as the original sample.
with open(RESULT_PATH, "r", encoding="utf-8") as file:
    result = json.load(file)

result["duration_ms"] = 118
with open(UPDATED_RESULT_PATH, "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4)

# dump(data, file) writes JSON to a file; dumps(data) returns JSON text.
json_text = json.dumps(result)
print("JSON text:", json_text)

# A JSON file should contain one complete document. To update it, load the
# document, change the Python object, and write the whole document back.

# Malformed JSON raises JSONDecodeError.
invalid_json = '{"status": PASS}'
try:
    json.loads(invalid_json)
except json.JSONDecodeError as error:
    print("Invalid JSON:", error)
