class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, child):
        self.children.append(child)


# Hàm thêm node
def add_node(value):
    temp = Node(value)
    return