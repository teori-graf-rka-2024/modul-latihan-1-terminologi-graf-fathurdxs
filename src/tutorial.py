import graph

def test_graph_functions():
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    G = graph.create_graph(edges)
    
    print("\nDerajat simpul:")
    for node in range(1, 6):
        print(f"Node {node}: {graph.get_degree(G, node)}")
    
    print("\nDFS Traversal dari simpul 1:")
    print(graph.dfs_traversal(G, 1))
    
    print("\nBFS Traversal dari simpul 1:")
    print(graph.bfs_traversal(G, 1))
    
    print("\nJalur Terpendek dari 1 ke 5:")
    print(graph.find_shortest_path(G, 1, 5))
    
    print("\nVisualisasi Graf:")
    graph.visualize_graph(G)

if __name__ == "__main__":
    test_graph_functions()
