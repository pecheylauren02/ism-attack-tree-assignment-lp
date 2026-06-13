def calculate_risk(node):
    """
    Recursive risk calculation:
    - LEAF: probability × impact
    - AND: sum of children
    - OR: max of children
    """

    if node["type"] == "LEAF":
        return node.get("probability", 0) * node.get("impact", 0)

    children = node.get("children", [])
    child_risks = [calculate_risk(c) for c in children]

    if node["type"] == "AND":
        return sum(child_risks)

    if node["type"] == "OR":
        return max(child_risks)

    return 0