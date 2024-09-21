class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Append a node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, new node is both head and tail
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node  # Update the current tail's next reference
        new_node.prev = self.tail  # Set new node's prev reference to current tail
        self.tail = new_node  # Update the tail to the new node

    # Prepend a node at the start of the list
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, new node is both head and tail
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head  # Set new node's next reference to current head
        self.head.prev = new_node  # Update current head's prev reference
        self.head = new_node  # Update the head to the new node

    # Delete a node with a given value
    def delete_value(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                # If it's the head node
                if current_node == self.head:
                    self.head = current_node.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None  # If the list is now empty
                # If it's the tail node
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                current_node = None
                return
            current_node = current_node.next

    # Print the list in forward direction
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    # Print the list in reverse direction (using the tail)
    def print_reverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")