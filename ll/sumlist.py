# Generate a linked list containing the sum of the nodes of the two input linked lists
# e.g. Input: 
# List1: 5->6->3 // represents number 365 
# List2: 8->4->2 // represents number 248 
# Output: 
# Resultant list: 3->1->6 // represents number 613 
# Explanation: 365 + 248 = 613
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
    def sumlist(list1, list2) -> None:
        ptr1 = list1.head
        ptr2 = list2.head
        length1 = 0
        length2 = 0
       
        while ptr1: # Find length of first list
            length1 += 1
            ptr1 = ptr1.next
       
        while ptr2: # Find length of second list
            length2 += 1
            ptr2 = ptr2.next
       
        multiplier1 = 1 
        multiplier2 = 1
        
        ptr1 = list1.head
        ptr2 = list2.head
        sum1 = 0
        sum2 = 0
        while ptr1: 
            sum1 += (ptr1.data * multiplier1)
            multiplier1 *= 10
            ptr1 = ptr1.next
        while ptr2:
            sum2 += (ptr2.data * multiplier2)
            multiplier2 *= 10
            ptr2 = ptr2.next
        
        total = sum1 + sum2
        result = LinkedList()
        total = str(total)
        for i in total:
            result.push(int(i))
        return result


list1 = LinkedList()
list2 = LinkedList()
list1.push(3)
list1.push(6)
list1.push(5)
list2.push(2)
list2.push(4)
list2.push(8)
result = LinkedList.sumlist(list1, list2)
temp = result.head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
