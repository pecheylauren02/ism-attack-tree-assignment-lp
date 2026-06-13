# Loads the attack tree from a JSON file.
# JSON was chosen for its readability and Python supports it natively.

import json


def load_tree(file_path):
    """
    Opens a JSON file and returns the attack tree as a dictionary.
    Raises an error if the file doesn't exist or isn't valid JSON.
    """
    with open(file_path, "r") as f:
        return json.load(f)