# ispf_models.py
"""
This module contains implementations of traditional ISPF/SPF algorithms, including Dijkstra's algorithm and Incremental SPF.
"""
import heapq
import networkx as nx

# Function to run Dijkstra's algorithm
def run_dijkstra(graph, source_node):
    """
    Computes the shortest path from a source node to all other nodes using Dijkstra's algorithm.

    Parameters:
    - graph: A NetworkX graph object.
    - source_node: The node from which shortest paths are computed.

    Returns:
    - distances: A dictionary of shortest distances from the source to each node.
    """
    queue = [(0, source_node)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[source_node] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        for neighbor in graph.neighbors(current_node):
            weight = graph.edges[current_node, neighbor]['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Function for incremental SPF calculation
def incremental_spf(graph, updated_edges, prev_shortest_paths):
    """
    Implements Incremental SPF to recalculate shortest paths after a graph change.

    Parameters:
    - graph: A NetworkX graph object.
    - updated_edges: List of edges that have changed.
    - prev_shortest_paths: Previously computed shortest paths.

    Returns:
    - updated_paths: Updated shortest paths after changes.
    """
    updated_paths = prev_shortest_paths.copy()

    # Iterate through each updated edge
    for edge in updated_edges:
        u, v = edge
        if edge in graph.edges:
            # If the edge is added or its weight is updated
            new_weight = graph.edges[u, v]['weight']
        else:
            # If the edge is removed, set the weight to infinity
            new_weight = float('inf')

        # Check if the shortest path involving the edge is affected
        for source in graph.nodes:
            if prev_shortest_paths[source][v] > prev_shortest_paths[source][u] + new_weight:
                # Recalculate shortest paths from the affected source node
                updated_paths[source] = run_dijkstra(graph, source)
                break
    
    return updated_paths
