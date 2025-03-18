import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges: list[tuple[int, int]]):
    grafik = nx.Graph()
    grafik.add_edges_from(edges)
    print(grafik)
    return grafik

def get_degree(G: nx.graph, node: int):
    degree = int(G.degree(node))
    print(degree)
    return degree

def dfs_traversal(G: nx.graph, start: int):
    hasil_pencarian = []
    dikunjungi = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in dikunjungi:
            dikunjungi.add(node)
            hasil_pencarian.append(node)
            for adj in reversed(list(G.neighbors(node))):
                if adj not in dikunjungi:
                    stack.append(adj)
    for i in hasil_pencarian:
        print(i, end=" ")
    print()
    return hasil_pencarian

def bfs_traversal(G: nx.graph, start: int):
    hasil_pencarian = []
    dikunjungi = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in dikunjungi:
            dikunjungi.add(node)
            hasil_pencarian.append(node)
            for adj in G.neighbors(node):
                if adj not in dikunjungi:
                    queue.append(adj)
    for i in hasil_pencarian:
        print(i, end=" ")
    print()
    return hasil_pencarian

def find_shortest_path(G: nx.graph, source: int, target: int):
    path = nx.shortest_path(G, source, target)
    for i in path:
        print(i, end=" ")
    print()
    return path

def visualize_graph(G: nx.graph):
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=15)
    plt.show()
