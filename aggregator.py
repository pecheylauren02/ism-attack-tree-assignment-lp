# Calculates the overall risk score for an attack tree node.
# Risk model:
#   LEAF: probability x impact (expected monetary loss)
#   AND:  sum of children — all steps must succeed, so costs add up
#   OR:   max of children — only one path needs to succeed, so worst case wins


def calculate_risk(node):
    """
    Recursively calculates risk for a node and its children.
    Returns a monetary value (£).
    """

    if node["type"] == "LEAF":
        # Expected monetary value = likelihood x financial damage
        return node.get("probability", 0) * node.get("impact", 0)

    children = node.get("children", [])
    child_risks = [calculate_risk(child) for child in children]

    if node["type"] == "AND":
        # Attacker must complete every step, so risks accumulate
        return sum(child_risks)

    if node["type"] == "OR":
        # Attacker only needs one path to work, so we take the worst case
        return max(child_risks)

    # Unknown node type — return 0 so the rest of the tree still runs
    return 0
