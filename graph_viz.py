from graphviz import Digraph

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph[u]:
            self.graph[u].append(v)
        else:
            print(f"Линия {u} -> {v} уже существует.")

    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

    def visualize_graph(self):
        dot = Digraph()
        for node in self.graph:
            dot.node(str(node))
            for neighbor in self.graph[node]:
                dot.node(str(neighbor))
                dot.edge(str(node), str(neighbor))
        return dot

# Создание графа и добавление рёбер
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
# Попытка добавить существующую линию
g.add_edge(1, 4)

# Печать графа
g.print_graph()

# Визуализация графа
graph_dot = g.visualize_graph()
graph_dot.render('graph', format='png', view=True)  # Сохраняет изображение и открывает его
