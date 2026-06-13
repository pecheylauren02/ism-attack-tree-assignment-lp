import json

def load_tree(file_path):
    """Load attack tree JSON file"""
    with open(file_path, "r") as f:
        return json.load(f)