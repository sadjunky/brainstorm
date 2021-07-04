# Remove dupplicates from an unsorted linked list
from collections import defaultdict

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
    
    def remove_duplicates(self) -> None:
        hash = {} # To check whether duplicate keys are present
        temp = self.head
        hash[temp.data] = 1
        while temp:
            while True:
                if temp.next and (not (temp.next.data in hash)):
                    hash[temp.next.data] = 1
                    break
                else:
                    if temp.next:
                        temp.next = temp.next.next
                    else:
                        break
            temp = temp.next

l = LinkedList()
l.push(21)
l.push(43)
l.push(41)
l.push(21)
l.push(12)
l.push(11)
l.push(12)
l.remove_duplicates()
l.print()
