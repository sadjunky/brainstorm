# Cycle detection in a linked list
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def detect_and_count_loop(l) -> bool: # Using Floyd's cycle detection algorithm
    slow = l
    fast = l
    count = 0
    while fast is not None:
        if fast.next is None:
            raise RuntimeError("No loop detected")
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            count += 1  
            slow = slow.next
            while slow is not fast:
                count += 1
                slow = slow.next
            return count
    raise RuntimeError("No loop detected")

l = Node(1)
l.next = Node(2)
l.next.next = Node(3)
l.next.next.next = Node(4)
l.next.next.next.next = Node(5)
l.next.next.next.next.next = l.next

print(detect_and_count_loop(l))
