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