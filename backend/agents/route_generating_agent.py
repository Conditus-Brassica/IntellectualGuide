import osmnx as ox
import networkx as nx
from osmnx import distance

# Specify the name of the place
place_name = "Bangalore, India"

# Create a street network graph from the place
G = ox.graph_from_place(place_name, network_type='drive')

# Specify your origin and destination coordinates
orig_coords = (12.9715987, 77.5945627)  # Bangalore coordinates
dest_coords = (13.0827, 80.2707)  # Chennai coordinates

# Find the nodes nearest to the origin and destination coordinates
orig_node = ox.distance.nearest_nodes(G, orig_coords[1], orig_coords[0])
dest_node = ox.distance.nearest_nodes(G, dest_coords[1], dest_coords[0])

# Calculate the shortest path between the origin and destination nodes
shortest_path = nx.shortest_path(G, orig_node, dest_node, weight='length')

# Print the shortest path
for i in shortest_path:
    print(G[i])
