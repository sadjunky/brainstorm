# Reverse k pair nodes in a linked list
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def push(self, data) -> None:
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
    
    def print(self) -> None:
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    def reversek(self, head, k) -> Node:
        temp = head
        prev = None
        curr = temp
        count = 0
        while curr and count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        
        if temp:
            head.next = self.reversek(temp, k) # Attach the head of the reversed list to the head of the former reversed list
        
        return prev

l = LinkedList()
l.push(8)
l.push(7)
l.push(6)
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
head = l.reversek(l.head, 3)
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
