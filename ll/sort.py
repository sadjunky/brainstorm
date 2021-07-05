# Sort a linked list containing 0s, 1s, and 2s
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
    
    def sort(self) -> None:
        n1, n2, n3 = 0, 0, 0
        temp = self.head
        while temp:
            if temp.data == 0:
                n1 += 1
            if temp.data == 1:
                n2 += 1
            if temp.data == 2:
                n3 += 1
            temp = temp.next
        temp = self.head
        count = 0
        while temp:
            count += 1
            if count <= n1:
                temp.data = 0
            if count > n1 and count <= (n1+n2):
                temp.data = 1
            if count > (n1+n2) and count <= (n1+n2+n3):
                temp.data = 2
            temp = temp.next   

l = LinkedList()
l.push(1)
l.push(0)
l.push(2)
l.push(0)
l.push(2)
l.push(1)
l.push(1)
l.sort()
l.print()    
