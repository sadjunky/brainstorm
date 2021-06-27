# Basic operations on linked list
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def push_front(self, data) -> None:
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
    
    def push_after(self, prev, data) -> None:
        temp = self.head
        while temp is not None:
            if temp is prev:
                addr = temp.next
                temp.next = Node(data)
                temp.next.next = addr
                break
            temp = temp.next
    
    def push_rear(self, data) -> None:
        temp = self.head
        while temp is not None:
            if temp.next is None:
                temp.next = Node(data)
                break
            temp = temp.next
    
    def pop_iter(self, data) -> None:
        temp = self.head
        while temp is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                break
            temp = temp.next
        
        raise ValueError("Value not found")

    def pop_recur(self, data, temp=None) -> None:
        if temp is None:
            temp = self.head
        if temp.next is None and temp.data == data:
                return
        if temp.next.data == data:
            temp.next = temp.next.next
            return
        temp = temp.next
        if temp.next is None:
            raise ValueError("Value not found")
        self.pop_recur(data, temp)
    
    def pop_pos(self, pos) -> None:
        if pos < 0:
            raise IndexError("Index out of range")
        
        if pos == 0:
            self.head = self.head.next
            return
        
        position = 0
        temp = self.head
        while temp is not None:
            if position == pos - 1:
                temp.next = temp.next.next
                return
            temp = temp.next
            position += 1
        
        raise IndexError("Index out of range")
    
    def remove(self):
        while self.head is not None:
            self.head = self.head.next


l = LinkedList()
l.push_front(3)
l.push_front(2)
l.push_front(1)
l.push_rear(4)
l.push_rear(5)
l.push_after(l.head, 6)
l.remove()

print(l.head.data)
