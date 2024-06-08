import networkx as nx
import matplotlib.pyplot as plt
import random

# Створення графа
G = nx.Graph()

# Додавання вершин
devices = ["Router1", "Router2", "Switch1", "Switch2", "Switch3", "PC1", "PC2", "Printer1", "Printer2"]

for device in devices:
    G.add_node(device)

# Додавання ребер
edges = [("Router1", "Switch1"), ("Router1", "Switch2"), ("Router1", "Switch3"),
         ("Router2", "Switch1"), ("Router2", "Switch2"), ("Router2", "Switch3"),
         ("Switch1", "PC1"), ("Switch1", "Printer1"),
         ("Switch2", "PC2"), ("Switch2", "Printer2"),
         ("Switch3", "PC1"), ("Switch3", "PC2")]

# Додавання ваг до ребер
weighted_edges = [(u, v, random.randint(1, 10)) for u, v in edges]
G.add_weighted_edges_from(weighted_edges)

# Візуалізація графа з вагами ребер
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # seed для відтворюваності розташування вершин
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Корпоративна інтернет-мережа з вагами ребер")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин у графі:", G.number_of_nodes())
print("Кількість ребер у графі:", G.number_of_edges())
print("Ступінь кожної вершини:", dict(G.degree()))

# Знаходження найкоротших шляхів між усіма вершинами
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

# Виведення найкоротших шляхів
for source, paths in shortest_paths.items():
    for target, path in paths.items():
        print(f"Найкоротший шлях між {source} та {target}: {path}")

# Виведення довжин найкоротших шляхів
shortest_path_lengths = dict(nx.all_pairs_dijkstra_path_length(G))

# Виведення довжин найкоротших шляхів
for source, lengths in shortest_path_lengths.items():
    for target, length in lengths.items():
        print(f"Довжина найкоротшого шляху між {source} та {target}: {length}")
