# Circular Queue using Linked List with front and rear pointers
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None
    
    def enqueue(self, data):
        if not self.front:
            self.front = self.rear = Node(data)
            self.rear.next = self.front
            return
        self.rear.next = Node(data)
        self.rear = self.rear.next
        self.rear.next = self.front
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue underflow!"
        if self.front.data == self.front.next.data:
            temp = self.front
            self.front = self.rear = None
            return temp.data
        temp = self.front
        self.front = self.front.next
        self.rear.next = self.front
  
        if(self.front == None):
            self.rear = None
        return temp.data

        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print(q.dequeue())
print(q.dequeue())
