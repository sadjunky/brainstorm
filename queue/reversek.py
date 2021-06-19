# Reverse the first k elements
class Queue:

    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, data) -> None:
        self.queue.insert(0, data)
    
    def dequeue(self) -> int:
        return self.queue.pop()
    
    def size(self) -> int:
        return len(self.queue)

    def reverse(self, k) -> list:
        stack = []
        size = self.size()
        for i in range(size):
            if i >= (size - k):
               stack.insert(0, self.dequeue())
               continue
            self.enqueue(self.dequeue())
        while stack:
            self.enqueue(stack.pop(0)) 
            
        

q = Queue()
q.enqueue(10)
q.enqueue(9)
q.enqueue(8)
q.enqueue(7)
q.enqueue(6)
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.reverse(10)

print(q.queue)

