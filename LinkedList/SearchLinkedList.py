class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search_linked_list(head, X):
    current = head
    while current is not None:
        if current.data == X:
            return True
        current = current.next
    return False
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

X=20

print("Element found in linked list" if search_linked_list(head, X) else "Element not found in linked list")