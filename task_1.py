import networkx as nx
import matplotlib.pyplot as plt

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

G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # seed для відтворюваності розташування вершин
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title("Корпоративна інтернет-мережа")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин у графі:", G.number_of_nodes())
print("Кількість ребер у графі:", G.number_of_edges())
print("Ступінь кожної вершини:", dict(G.degree()))
