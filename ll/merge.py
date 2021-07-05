# Merge all nodes into a single linked list in ascending order
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

    @staticmethod
    def push_to_list(list, node) -> None:
        if not list.head:
            list.head = Node(node.data)
        else:
            temp = list.head
            list.head = Node(node.data)
            list.head.next = temp
    
    def print(self) -> None:
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    @staticmethod
    def merge(list1, list2) -> Node:
        ptr1 = list1.head
        ptr2 = list2.head
        merged = LinkedList()
        while ptr1 and ptr2:
            if ptr1.data < ptr2.data:
                LinkedList.push_to_list(merged, ptr1)
                ptr1 = ptr1.next
            elif ptr2.data < ptr1.data:
                LinkedList.push_to_list(merged, ptr2)
                ptr2 = ptr2.next
            else:
                LinkedList.push_to_list(merged, ptr2)
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            if ptr1 and not ptr2: # If we have reached the end of one of the lists
                while ptr1:
                    LinkedList.push_to_list(merged, ptr1)
                    ptr1 = ptr1.next
                break
            if ptr2 and not ptr1: # If we have reached the end of one of the lists
                while ptr2:
                    LinkedList.push_to_list(merged, ptr2)
                    ptr2 = ptr2.next
                break
        
        return merged

l1 = LinkedList()
l2 = LinkedList()
l1.push(40)
l1.push(15)
l1.push(10)
l1.push(5)
l2.push(20)
l2.push(3)
l2.push(2)
merged = LinkedList.merge(l1, l2)
temp = merged.head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
