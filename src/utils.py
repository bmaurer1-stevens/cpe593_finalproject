# utils.py
"""
This module contains utility functions such as logging and data handling.
"""
import json
import networkx as nx

def load_graph(filepath):
    """
    Loads a previously generated graph from a file.

    Parameters:
    - filepath: Path to the graph file.

    Returns:
    - graph: A NetworkX graph object.
    """
    with open(filepath, 'r') as f:
        data = json.load(f)
    return nx.node_link_graph(data)

def log_metrics(metrics, filename):
    """
    Logs benchmarking metrics.

    Parameters:
    - metrics: Dictionary of metrics to log.
    - filename: Name of the file to store the logs.
    """
    with open(f"../logs/simulation_logs/{filename}.json", 'w') as f:
        json.dump(metrics, f)

