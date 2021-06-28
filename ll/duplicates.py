# Remove duplicates from a sorted linked list
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
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
    
    def print(self) -> None:
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next 
    
    def remove_duplicates(self) -> None:
        temp = self.head
        while temp is not None:
            ptr = temp
            while ptr.next and ptr.data == ptr.next.data:
                ptr.next = ptr.next.next
            temp = temp.next

l = LinkedList()
l.push(60)
l.push(43)
l.push(43)
l.push(21)
l.push(11)
l.push(11)
l.push(11)
l.remove_duplicates()

l.print()
