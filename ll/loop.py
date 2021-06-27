# Cycle detection in a linked list
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def detect_loop(l): # Using Floyd's cycle detection algorithm
    slow = l
    fast = l
    while fast is not None:
        if fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return True
    return False

l = Node(1)
l.next = Node(2)
l.next.next = Node(3)
l.next.next.next = Node(4)
l.next.next.next.next = Node(5)
l.next.next.next.next.next = Node(6)

print(detect_loop(l))
