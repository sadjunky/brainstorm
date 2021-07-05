# Rotate a linked list counter clockwise by k times
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
    
    def rotate(self, k) -> None:
        temp = self.head
        count = 0
        while temp:
            count += 1
            if count == k:
                ptr = temp.next
                temp.next = None
                head = self.head
                self.head = ptr
                while ptr.next:
                    ptr = ptr.next
                ptr.next = head
                break
            temp = temp.next

l = LinkedList()
l.push(60)
l.push(50)
l.push(40)
l.push(30)
l.push(20)
l.push(10)
l.rotate(4)
l.print()
