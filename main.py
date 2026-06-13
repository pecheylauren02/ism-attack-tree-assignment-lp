from attack_tree import load_tree
from aggregator import calculate_risk
from visualiser import draw_tree
import matplotlib.pyplot as plt


def prompt_leaf_values(node):
    """
    Walks the tree and asks the user to enter probability and impact
    for each leaf node. Loops until valid input is given.
    """
    if node["type"] == "LEAF":
        print(f"\n  Node: {node['name']}")
        while True:
            try:
                prob = float(input("    Probability (0.0–1.0): "))
                if 0.0 <= prob <= 1.0:
                    node["probability"] = prob
                    break
                print("    Must be between 0 and 1.")
            except ValueError:
                print("    Enter a number.")

        while True:
            try:
                impact = float(input("    Impact (£): "))
                if impact >= 0:
                    node["impact"] = impact
                    break
                print("    Can't be negative.")
            except ValueError:
                print("    Enter a number.")

    for child in node.get("children", []):
        prompt_leaf_values(child)


def analyse(file_path, label):
    """Loads the tree, collects user input, draws it, and returns the risk."""
    print(f"\n{'='*50}\n  {label}\n{'='*50}")
    tree = load_tree(file_path)
    print("\nEnter values for each leaf node:")
    prompt_leaf_values(tree)
    draw_tree(tree, title=label)
    risk = calculate_risk(tree)
    print(f"\n  {label} Risk: £{risk:,.2f}")
    return risk