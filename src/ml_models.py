# ml_models.py
"""
This module implements machine learning models such as Graph Neural Networks (GNNs) and reinforcement learning agents to solve the pathfinding problem.
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torch_geometric.nn import GCNConv

# Define a simple GCN model
class GCNModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        """
        Initializes the GCN model.

        Parameters:
        - input_dim: Input feature size.
        - output_dim: Output feature size.
        """
        super(GCNModel, self).__init__()
        self.conv1 = GCNConv(input_dim, 16)
        self.conv2 = GCNConv(16, output_dim)
    
    def forward(self, x, edge_index):
        """
        Forward pass through the GCN.

        Parameters:
        - x: Node feature matrix.
        - edge_index: Graph edge list.


        Returns:
        - x: Output after forward pass.
        """
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x

# Function to train the GCN model
def train_gnn_model(model, data_loader, epochs):
    """
    Trains the GCN model.

    Parameters:
    - model: GCN model to be trained.
    - data_loader: Data loader for input data.
    - epochs: Number of epochs to train.
    """
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()
    
    for epoch in range(epochs):
        model.train()
        for data in data_loader:
            optimizer.zero_grad()
            out = model(data.x, data.edge_index)
            loss = criterion(out, data.y)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")
