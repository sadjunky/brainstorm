# Queue using Linked List with front and rear pointers
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
            return
        self.rear.next = Node(data)
        self.rear = self.rear.next
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue underflow!"
        temp = self.front
        self.front = self.front.next
  
        if(self.front == None):
            self.rear = None
        return temp.data

        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print("Queue front " + str(q.front.data))
print("Queue rear " + str(q.rear.data))
