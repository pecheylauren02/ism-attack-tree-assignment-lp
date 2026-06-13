# Builds and displays the attack tree as a graph using NetworkX and Matplotlib.
# I used a hierarchical layout instead of spring_layout because spring_layout
# produces a web shape, which doesn't make sense for a tree structure.

import networkx as nx
import matplotlib.pyplot as plt


def build_graph(G, node, parent=None):
    """Recursively adds nodes and edges to the graph."""
    G.add_node(node["name"])
    if parent:
        G.add_edge(parent, node["name"])
    for child in node.get("children", []):
        build_graph(G, child, node["name"])


def hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0.0, xcenter=0.5):
    """
    Returns x/y positions laid out as a top-down tree.
    Adapted from: https://stackoverflow.com/a/29597209
    """
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter, pos={})


def _hierarchy_pos(G, node, width, vert_gap, vert_loc, xcenter, pos):
    """Helper that assigns each node a position based on depth and siblings."""
    pos[node] = (xcenter, vert_loc)
    children = list(G.successors(node))
    if children:
        dx = width / len(children)
        start_x = xcenter - width / 2 + dx / 2
        for i, child in enumerate(children):
            _hierarchy_pos(G, child, dx, vert_gap, vert_loc - vert_gap, start_x + i * dx, pos)
    return pos


def draw_tree(tree, title="Attack Tree"):
    """Renders the attack tree as a hierarchical directed graph."""
    G = nx.DiGraph()
    build_graph(G, tree)

    pos = hierarchy_pos(G, root=tree["name"], width=2.0, vert_gap=0.3)

    plt.figure(figsize=(12, 7))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue",
            font_size=9, font_weight="bold", arrows=True, arrowsize=15)
    plt.title(title, fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.show()