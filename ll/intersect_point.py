# Find the intersection point between two linked lists
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
    def intersect_point(list1, list2) -> Node:
        ptr1 = list1.head
        ptr2 = list2.head
        
        while ptr1.next:
            ptr1 = ptr1.next
        
        while ptr2.next:
            ptr2 = ptr2.next
        
        if ptr1 is ptr2: # Check whether the final node of both the lists are equal
            return True
        return False

l1 = LinkedList()
l2 = LinkedList()
l1.push(30)
l1.push(15)
l1.push(9)
l1.push(6)
l1.push(3)
l2.push(10)
l2.head.next = l1.head.next.next.next
print(LinkedList.intersect_point(l1, l2))
