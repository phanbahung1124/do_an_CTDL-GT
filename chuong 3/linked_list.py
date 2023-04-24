class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Node không tồn tại")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def delete_node_at_pos(self, pos):
        current = self.head

        if pos == 0:
            self.head = current.next
            current = None
            return

        prev = None
        count = 0
        while current and count != pos:
            prev = current
            current = current.next
            count += 1

        if current is None:
            return

        prev.next = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

