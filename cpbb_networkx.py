# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Sample transaction data
transactions = pd.DataFrame({
    "From Account": ["Account A", "Account A", "Account B", "Account C", "Account C"],
    "To Account": ["Account B", "Account C", "Account C", "Account A", "Account B"],
    "Amount (USD)": [1000, 500, 700, 2000, 1500]
})



# Create a directed graph
G = nx.DiGraph()

# Add edges with weights (transaction amounts)
for _, row in transactions.iterrows():
    G.add_edge(row["From Account"], row["To Account"], weight=row["Amount (USD)"])

# Extract edge weights for visualization
edges, weights = zip(*nx.get_edge_attributes(G, 'weight').items())

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Layout for consistent graph position
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, edge_color="gray", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"${d['weight']}" for u, v, d in G.edges(data=True)}, font_size=8)
plt.title("Transaction Flow Between Accounts")
plt.show()
