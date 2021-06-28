class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

def mid_node(l) -> Node:
    temp = l.head
    count = 1
    while temp is not None:
        count += 1
        temp = temp.next
    if count % 2 == 0:
        mid_count = (count//2) + 1
    else:
        mid_count = count//2
    temp = l.head
    count = 1
    while temp is not None:
        count += 1
        if count == mid_count:
            return temp
        temp = temp.next

def reverse(head) -> Node:
    curr = head
    prev = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def check(ptr1, ptr2) -> bool:
    while ptr1 is not None and ptr2 is not None:
        if ptr1.data != ptr2.data:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return True

def palindrome(l):
    mid = mid_node(l)
    temp = l.head
    while temp is not None:
        if temp is mid:
            head = reverse(temp.next)
            temp.next = head
            return check(l.head, temp.next)
        temp = temp.next


l = LinkedList()
l.head = Node("M")
l.head.next = Node("A") 
l.head.next.next = Node("L")
l.head.next.next.next = Node("A")
l.head.next.next.next.next = Node("Y")
l.head.next.next.next.next.next = Node("A")
l.head.next.next.next.next.next.next = Node("L")
l.head.next.next.next.next.next.next.next = Node("A")
l.head.next.next.next.next.next.next.next.next = Node("M")

print(palindrome(l))
