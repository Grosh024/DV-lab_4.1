import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

st.title("Friendship Network Analysis")

# Define nodes and edges
nodes = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"]
edges = [
    ("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Charlie"), ("Charlie", "Diana"), ("Diana", "Eve"),
    ("Bob", "Diana"), ("Frank", "Eve"), ("Eve", "Ian"), ("Diana", "Ian"), ("Ian", "Grace"),
    ("Grace", "Hannah"), ("Hannah", "Jack"), ("Grace", "Jack"), ("Charlie", "Frank"), ("Alice", "Eve"), ("Bob", "Jack")
]

# Create graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

st.subheader("Task 1: Network Visualization")
fig, ax = plt.subplots(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500,
        font_size=10, font_weight='bold', edge_color='gray', ax=ax)
st.pyplot(fig)

st.subheader("Task 2: Degree Analysis")
degrees = dict(G.degree())
max_degree_node = max(degrees, key=degrees.get)
st.write("Degrees of each node:", degrees)
st.write(f"Most connected person: **{max_degree_node}** with {degrees[max_degree_node]} connections")

st.subheader("Task 3: Centrality Measures")
betweenness = nx.betweenness_centrality(G)
closeness = nx.closeness_centrality(G)
st.write("Betweenness Centrality:", betweenness)
st.write("Closeness Centrality:", closeness)

st.subheader("Task 4: Community Detection")
communities = greedy_modularity_communities(G)
for i, community in enumerate(communities, 1):
    st.write(f"Community {i}: {list(community)}")

# Assign a unique color to each community
palette = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple"]
node_to_comm = {}

for c_index, comm in enumerate(communities):
    for node in comm:
        node_to_comm[node] = c_index

# Build list of colors for drawing
community_colors = [palette[node_to_comm[n]] for n in G.nodes()]

# Draw graph again with community colors
plt.figure(figsize=(8,6))
nx.draw(
    G, pos, with_labels=True, node_size=3000,
    node_color=community_colors, edge_color="gray",
    font_size=10, font_weight="bold", arrows=True
)
# Draw edge labels (weights)
nx.draw_networkx_edge_labels(G, pos)
plt.title("Friendship Network Colored by Community")
plt.show()

st.subheader("Task 5: Most Influential Person")
degree_centrality = nx.degree_centrality(G)
most_influential = max(degree_centrality, key=degree_centrality.get)
st.write(f"Most influential person: **{most_influential}** (Centrality: {degree_centrality[most_influential]:.4f})")

fig, ax = plt.subplots(figsize=(8, 6))
node_colors = ['red' if node == most_influential else 'skyblue' for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500,
        font_size=10, font_weight='bold', edge_color='gray', ax=ax)
st.pyplot(fig)