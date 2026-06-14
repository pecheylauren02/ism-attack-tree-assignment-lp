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


def main():
    print("\n=== ATTACK TREE RISK ANALYSIS TOOL ===")

    pre = analyse("pre_tree.json", "PRE-DIGITALISATION")
    post = analyse("post_tree.json", "POST-DIGITALISATION")

    reduction = ((pre - post) / pre) * 100 if pre > 0 else 0.0

    print("\n=== SUMMARY ===")
    print(f"  Pre-Digitalisation Risk:  £{pre:,.2f}")
    print(f"  Post-Digitalisation Risk: £{post:,.2f}")
    print(f"  Risk Reduction:           {reduction:.2f}%")

    # Bar chart comparing both scenarios
    labels = ["Pre-Digitalisation", "Post-Digitalisation"]
    values = [pre, post]
    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=["tomato", "steelblue"])
    for bar, val in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + max(values) * 0.01,
                 f"£{val:,.0f}", ha="center", fontsize=11)
    plt.title("Risk Comparison: Pre vs Post Digitalisation")
    plt.ylabel("Expected Risk (£)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
