import graph as g

print("Grafik yang di inisialisasi:")
grafik = g.create_graph([(0, 5), (0, 4), (0, 2), (1, 5), (1, 4), (2, 4), (2, 3), (4, 5)])

print("derajat dari vertex 1:")
g.get_degree(grafik, 1)

print("dfs dengan stack(start node=5):")
g.dfs_traversal(grafik, 5)

print("bfs dengan queue(start node=0):")
g.bfs_traversal(grafik, 0)

print("mencari path terpendek dari vertex 2 ke 4:")
g.find_shortest_path(grafik, 2, 4)

g.visualize_graph(grafik)
