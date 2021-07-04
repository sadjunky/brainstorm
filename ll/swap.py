# Swap two random keys in a linked list
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
    
    def swap(self, key1, key2) -> None:
        ptr1 = self.head
        
        if ptr1.data in (key1, key2): # If one of the keys is present at the head
            ptr2 = ptr1.next
            if ptr2 and ptr2.data in (key1, key2): # If both of the keys are adjacent to each other
                temp = ptr2.next
                self.head = ptr2
                self.head.next = ptr1
                self.head.next.next = temp
                return
            while ptr2:
                if ptr2.next and (ptr2.next.data in (key1, key2)):
                    temp1 = ptr1
                    next1 = ptr1.next
                    temp2 = ptr2.next
                    next2 = ptr2.next.next
                    self.head = temp2
                    self.head.next = next1
                    ptr2.next = temp1
                    ptr2.next.next  = next2
                    return
                ptr2 = ptr2.next
        
        while ptr1:
            if ptr1.next and (ptr1.next.data in (key1, key2)):
                ptr2 = ptr1.next.next
                
                if ptr2 and ptr2.data in (key1, key2): # If both of the keys are adjacent and one of them is not at the head of the list
                    temp1 = ptr1.next
                    temp2 = ptr2.next
                    ptr1.next = ptr2
                    ptr1.next.next = temp1
                    ptr1.next.next.next = temp2
                    return
                
                while ptr2:
                    if ptr2.next and (ptr2.next.data in (key1, key2)): # If none of them are at the ends of the list
                        temp1 = ptr1.next
                        next1 = ptr1.next.next
                        temp2 = ptr2.next
                        next2 = ptr2.next.next
                        ptr1.next = temp2
                        ptr1.next.next = next1
                        ptr2.next = temp1
                        ptr2.next.next = next2
                        return
                    
                    ptr2 = ptr2.next
            
            ptr1 = ptr1.next
        
        raise KeyError("Key or keys not found")

l = LinkedList()
l.push(14)
l.push(20)
l.push(13)
l.push(12)
l.push(15)
l.push(10)
l.swap(12, 13)
l.print()
