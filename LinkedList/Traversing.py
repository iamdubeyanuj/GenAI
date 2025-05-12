class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def print_list(head):
    current = head
    while current is not None:
        print(current.key)
        current = current.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print_list(head)

class Solution :
    def getCount(self, head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count
    
count = Solution()
print(count.getCount(head))