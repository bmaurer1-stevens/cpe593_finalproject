# evaluation.py
"""
This module is responsible for evaluating and comparing the ISPF/SPF and ML models.
"""
import pandas as pd
from network_simulation import simulate_network_event as sne
import time
import tracemalloc

# Function to evaluate accuracy
def evaluate_accuracy(model, test_data):
    """
    Evaluates the accuracy of a given model.

    Parameters:
    - model: The model to be evaluated.
    - test_data: Test dataset.

    Returns:
    - accuracy: Accuracy metric for the model.
    """
    correct_predictions = 0
    total_predictions = len(test_data)

    for data in test_data:
        predicted_paths = model(data['graph'], data['source'])
        if predicted_paths == data['expected_paths']:
            correct_predictions += 1

    accuracy = correct_predictions / total_predictions
    return accuracy

# Function to benchmark performance
def benchmark_performance(models, graph, event_sequence):
    """
    Benchmarks the performance of different models.

    Parameters:
    - models: List of models to be evaluated.
    - graph: A NetworkX graph object.
    - event_sequence: Sequence of network events to simulate.
    
    Returns:
    - result_df: Dataframe of benchmark results.
    """
    results = []
    for event in event_sequence:
        sne(graph, event)
        for model in models:
            # Measure runtime
            start_time = time.time()
            model(graph)
            end_time = time.time()
            runtime = end_time - start_time

            # Measure memory usage
            tracemalloc.start()
            model(graph)
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            results.append({
                'model': model.__name__,
                'event': event,
                'runtime': runtime,
                'memory_peak_kb': peak / 1024
            })
    
    result_df = pd.DataFrame(results)
    result_df.to_csv("../results/comparison_results.csv", index=False)
    return result_df
