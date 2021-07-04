# Find common elements between two linked lists
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
    
    @staticmethod
    def intersection(list1, list2) -> Node:
        ptr1 = list1.head
        ptr2 = list2.head
        intersect = None
        while ptr1 and ptr2: 
            if ptr1.data < ptr2.data:
                ptr1 = ptr1.next
            elif ptr2.data < ptr1.data:
                ptr2 = ptr2.next
            else:
                if not intersect:
                    intersect = Node(ptr1.data)
                else:
                    temp = intersect
                    while temp:
                        if not temp.next:
                            temp.next = Node(ptr1.data)
                            break
                        temp = temp.next
                ptr1 = ptr1.next
                ptr2 = ptr2.next

        return intersect

l1 = LinkedList()
l2 = LinkedList()
l1.push(6)
l1.push(5)
l1.push(4)
l1.push(3)
l1.push(2)
l1.push(1)
l2.push(8)
l2.push(6)
l2.push(4)
l2.push(2)
list = LinkedList.intersection(l1, l2)
temp = list
while temp:
    print(temp.data, end=" ")
    temp = temp.next
