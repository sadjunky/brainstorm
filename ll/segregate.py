# Segregate a linked list based on even and odd. All even numbers are at the front of the list and odd numbers are at the rear of the list. Order is to be maintained
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
    
    def segregate(self) -> None:
        tail = self.head
        length = 1
        while tail.next: # Reach the tail of the linked list and calculate the length
            length += 1
            tail = tail.next
        temp = self.head
        
        while temp.data % 2 != 0 and length > 0: # Move all odd nodes before an even node to the end of the list
            self.head = temp.next
            tail.next = temp
            tail.next.next = None
            tail = tail.next
            temp = self.head
            length -= 1
        
        while temp and length > 1:
            while True and length > 1:
                if temp.next and temp.next.data % 2 != 0:
                    ptr = temp.next
                    temp.next = temp.next.next
                    tail.next = ptr
                    tail.next.next = None
                    tail = tail.next
                    length -= 1
                else:
                    break
            temp = temp.next
            length -= 1

l = LinkedList()
l.push(6)
l.push(7)
l.push(1)
l.push(4)
l.push(5)
l.push(10)
l.push(12)
l.push(8)
l.push(15)
l.push(17)
l.segregate()
l.print()
