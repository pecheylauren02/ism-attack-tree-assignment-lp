# Unit tests for the calculate_risk function.
# Run with: pytest test_aggregator.py -v

from aggregator import calculate_risk


def leaf(name, prob, impact):
    return {"name": name, "type": "LEAF", "probability": prob, "impact": impact}


def test_leaf_basic():
    assert calculate_risk(leaf("Test", 0.5, 10000)) == 5000.0


def test_leaf_zero_prob():
    assert calculate_risk(leaf("Test", 0.0, 10000)) == 0.0


def test_leaf_zero_impact():
    assert calculate_risk(leaf("Test", 0.9, 0)) == 0.0


def test_or_takes_max():
    node = {
        "name": "Root", "type": "OR",
        "children": [leaf("A", 0.5, 10000), leaf("B", 0.8, 120000)]
    }
    assert calculate_risk(node) == 96000.0  # max(5000, 96000)


def test_and_sums_children():
    node = {
        "name": "Root", "type": "AND",
        "children": [leaf("A", 0.5, 10000), leaf("B", 0.8, 5000)]
    }
    assert calculate_risk(node) == 9000.0  # 5000 + 4000


def test_unknown_type():
    assert calculate_risk({"name": "X", "type": "XOR", "children": []}) == 0