# Nhập mọi thứ từ cay.py
from tree import *


# Duyệt theo thứ tự trước dùng đệ quy: Node -> Left -> Right, bắt đầu từ nút gốc
def preorder_traversal(node):
    print(node.value, end=" ")  # In giá trị của nút ra
    if len(node.children) != 0:  # Kiểm tra nếu nút có con, nếu có thì duyệt các nút con từ trái -> phải
        for i in range(0, len(node.children)):
            preorder_traversal(node.children[i])


# Duyệt theo thứ tự sau dùng đệ quy: Left -> Right -> Node, bắt đầu từ nút gốc
def postorder_traversal(node):
    if len(node.children) != 0: # Kiểm tra nếu nút có con, nếu có thì duyệt các nút con từ trái -> phải
        for i in range(0, len(node.children)):
            postorder_traversal(node.children[i])
    print(node.value, end=" ")  # In giá trị của nút ra


if __name__ == "__main__":
    '''
    Giả sử muốn tạo cây như bên dưới
                  5
               /    \   \
              7     3     8
           /  \     |   /  | \
          4   2     1   9  6  2
    Ta viết như sau
    '''
    root = add_node(5)
    root.add_child(add_node(7))
    root.add_child(add_node(3))
    root.add_child(add_node(8))
    root.children[0].add_child(add_node(4))
    root.children[0].add_child(add_node(2))
    root.children[1].add_child(add_node(1))
    root.children[2].add_child(add_node(9))
    root.children[2].add_child(add_node(6))
    root.children[2].add_child(add_node(2))

    preorder_traversal(root)
    print()
    postorder_traversal(root)