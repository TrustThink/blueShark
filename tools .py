import os
import json                

# Tool: Write JSON file
# input: filepath (string), data (python dict)
# returns: nothing

def write_json_file(filepath: str, data: dict) -> None:
    """
    Creates a JSON file at the given filepath
    using the provided Python dictionary.
    """

    # Make sure folder exists
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    # Write dictionary to JSON file
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

# Example test data ( check if function works)
example_data = {
    "test": 1
}

# Call the function
write_json_file("case/test/inventory/protocols.json", example_data)

# Reads a JSON file and returns its contents as a Python dictionary.
# Returns empty dictionary {} if the file does not exist or is invalid.

def read_json_safe(filepath: str) -> dict:
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
