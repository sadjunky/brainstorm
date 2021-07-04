# Swap a linked list in pairs
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
    
    def swap_pair(self) -> None:
        ptr1 = self.head
        ptr2 = self.head.next
        next1 = ptr2.next
        self.head = ptr2
        self.head.next = ptr1
        self.head.next.next = next1
        
        temp = self.head.next
        if not temp.next:
            return 
        
        while temp and temp.next and temp.next.next and temp.next.next.next:
            if not temp.next:
                return
            ptr1 = temp.next
            ptr2 = temp.next.next
            next1 = ptr2.next
            temp.next = ptr2
            temp.next.next = ptr1
            temp.next.next.next = next1

            temp = temp.next.next

l = LinkedList()
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.swap_pair()
l.print()
