import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин
devices = ["Router1", "Router2", "Switch1", "Switch2", "Switch3", "PC1", "PC2", "Printer1", "Printer2"]

for device in devices:
    G.add_node(device)

# Додавання ребер з вагами
edges = [("Router1", "Switch1", 1), ("Router1", "Switch2", 2), ("Router1", "Switch3", 3),
         ("Router2", "Switch1", 4), ("Router2", "Switch2", 5), ("Router2", "Switch3", 6),
         ("Switch1", "PC1", 7), ("Switch1", "Printer1", 8),
         ("Switch2", "PC2", 9), ("Switch2", "Printer2", 10),
         ("Switch3", "PC1", 11), ("Switch3", "PC2", 12)]

G.add_weighted_edges_from(edges)

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

# Застосування алгоритму Дейкстри для знаходження найкоротшого шляху між всіма вершинами графа
for device1 in devices:
    for device2 in devices:
        if device1 != device2:
            shortest_path = nx.dijkstra_path(G, device1, device2)
            print(f"Найкоротший шлях від {device1} до {device2}: {' -> '.join(shortest_path)}")
