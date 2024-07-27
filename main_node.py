# формирование дерева
from graphviz import Digraph

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функция для добавления нового узла
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Функция для создания графа дерева
def add_nodes_edges(dot, node):
    if node is not None:
        if node.left:
            dot.node(str(node.left.val))
            dot.edge(str(node.val), str(node.left.val))
            add_nodes_edges(dot, node.left)
        if node.right:
            dot.node(str(node.right.val))
            dot.edge(str(node.val), str(node.right.val))
            add_nodes_edges(dot, node.right)

def visualize_tree(root):
    dot = Digraph()
    if root is not None:
        dot.node(str(root.val))
        add_nodes_edges(dot, root)
    return dot

# Пример использования
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Визуализация дерева
tree_dot = visualize_tree(root)
tree_dot.render('binary_tree', format='png', view=True)  # Сохраняет изображение и открывает его
