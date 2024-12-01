# graph_generation.py
"""
This module handles the generation of synthetic graph data for testing ISPF/SPF and ML models.
"""
import networkx as nx
import random
import json

# Function to generate random graphs
def generate_random_graphs(num_nodes, edge_density, weight_distribution):
    """
    Generates a random graph using NetworkX.

    Parameters:
    - num_nodes: Number of nodes in the graph.
    - edge_density: Probability of edge creation.
    - weight_distribution: Type of weight distribution for edges.

    Returns:
    - graph: A NetworkX graph object.
    """
    graph = nx.gnp_random_graph(num_nodes, edge_density, directed=True)
    
    for (u, v) in graph.edges():
        graph.edges[u, v]['weight'] = random.uniform(1, 10) if weight_distribution == 'uniform' else random.randint(1, 100)
    
    return graph

# Function to save the generated graph
def save_graph(graph, filename):
    """
    Saves the generated graph in a JSON format.

    Parameters:
    - graph: A NetworkX graph object.
    - filename: Name of the file where the graph will be saved.
    """
    data = nx.node_link_data(graph)
    with open(filename, 'w') as f:
        json.dump(data, f)

# Sample usage
graph = generate_random_graphs(10, 0.3, 'uniform')
save_graph(graph, "../data/generated_graphs/random_graph.json")
