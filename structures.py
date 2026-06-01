deleted_stack = []

task_queue = []


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def get_all(self):

        result = []

        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result


history = LinkedList()

