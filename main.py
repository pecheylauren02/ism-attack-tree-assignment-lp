from attack_tree import load_tree
from aggregator import calculate_risk
from visualiser import draw_tree

import matplotlib.pyplot as plt


def analyse(file_path, label):
    print(f"\n--- {label} ---")

    tree = load_tree(file_path)

    draw_tree(tree, label)

    risk = calculate_risk(tree)

    print(f"{label} Risk: £{risk:,.2f}")

    return risk


def main():

    print("\n=== ATTACK TREE RISK ANALYSIS TOOL ===")

    pre = analyse("pre_tree.json", "PRE-DIGITALISATION")
    post = analyse("post_tree.json", "POST-DIGITALISATION")

    reduction = ((pre - post) / pre) * 100

    print("\n=== SUMMARY ===")
    print(f"Risk Reduction: {reduction:.2f}%")

    labels = ["Pre", "Post"]
    values = [pre, post]

    plt.bar(labels, values)
    plt.title("Risk Comparison")
    plt.ylabel("Risk (£)")
    plt.show()


if __name__ == "__main__":
    main()