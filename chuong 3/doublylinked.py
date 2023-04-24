class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
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
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Node không tồn tại")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def delete_node(self, key):
        current = self.head

        if current and current.data == key:
            if current.next:
                current.next.prev = None
            self.head = current.next
            current = None
            return

        while current and current.data != key:
            current = current.next

        if current is None:
            return

        if current.next:
            current.next.prev = current.prev
        current.prev.next = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
