# Reverse a Linked List
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
    
    def reverse(self) -> None:
        temp = self.head
        prev = None
        curr = temp
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        self.head = prev
    
    def print_reverse(self, node) -> None: # Print reverse of a linked list without actually reversing the list
        if not node.next:
            print(node.data, end=" ")
            return
        self.print_reverse(node.next)
        print(node.data, end=" ")


l = LinkedList()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.print_reverse(l.head)
l.reverse()
