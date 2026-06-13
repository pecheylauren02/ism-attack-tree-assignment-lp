import networkx as nx
import matplotlib.pyplot as plt


def build_graph(G, node, parent=None):
    """
    Recursively build a NetworkX graph from a nested tree structure.

    Args:
        G (nx.DiGraph): Graph object being built.
        node (dict): Current node with 'name' and optional 'children'.
        parent (str, optional): Parent node name.
    """
    G.add_node(node["name"])

    if parent:
        G.add_edge(parent, node["name"])

    for child in node.get("children", []):
        build_graph(G, child, node["name"])


def draw_tree(tree, title="Attack Tree"):
    """
    Visualise an attack tree using NetworkX and Matplotlib.

    Args:
        tree (dict): Root node of the attack tree.
        title (str): Plot title.
    """
    G = nx.DiGraph()
    build_graph(G, tree)

    plt.figure(figsize=(12, 7))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        font_size=9,
        arrows=True
    )

    plt.title(title)
    plt.show()