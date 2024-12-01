# network_simulation.py
"""
This module simulates changes in the network and measures the response of each algorithm.
"""
import random
import networkx as nx

def simulate_network_event(graph, event_type):
    """
    Simulates network changes such as adding/removing nodes or edges.

    Parameters:
    - graph: A NetworkX graph object.
    - event_type: Type of event to simulate ('node_failure', 'link_failure', 'link_recovery').
    """
    if event_type == 'node_failure':
        node = random.choice(list(graph.nodes))
        graph.remove_node(node)
    elif event_type == 'link_failure':
        edge = random.choice(list(graph.edges))
        graph.remove_edge(*edge)
    elif event_type == 'link_recovery':
        # Adding a link back (if it previously existed)
        available_nodes = list(graph.nodes)
        if len(available_nodes) > 1:
            node1, node2 = random.sample(available_nodes, 2)
            if not graph.has_edge(node1, node2):
                graph.add_edge(node1, node2, weight=random.uniform(1, 10))

# Function to simulate path updates
def simulate_path_updates(graph, models, events):
    """
    Simulates network events and updates paths using the given models.

    Parameters:
    - graph: A NetworkX graph object.
    - models: List of models to be evaluated.
    - events: List of events to simulate.
    """
    for event in events:
        simulate_network_event(graph, event)
        for model in models:
            if hasattr(model, 'run_dijkstra'):
                # If the model is traditional Dijkstra or Incremental SPF
                source_node = random.choice(list(graph.nodes))
                shortest_paths = model.run_dijkstra(graph, source_node)
                print(f"Model: {model.__name__}, Event: {event}, Source: {source_node}, Shortest Paths: {shortest_paths}")
            elif hasattr(model, 'predict'):
                # If the model is an ML-based model
                shortest_paths = model.predict(graph)
                print(f"Model: {model.__name__}, Event: {event}, Predicted Shortest Paths: {shortest_paths}")
