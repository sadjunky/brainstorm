# Reverse using iteration and recursion
class Queue:

    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, data) -> None:
        self.queue.insert(0, data)
    
    def dequeue(self) -> int:
        return self.queue.pop()
    
    def empty(self) -> bool:
        return len(self.queue) == 0

    def reverse_recursion(self) -> None:
        if not self.queue:
            return
        temp = self.dequeue()
        self.reverse_recursion()
        self.enqueue(temp)
    
    def reverse_iteration(self) -> None:
        stack = []
        while self.queue:
            stack.append(self.dequeue())
        while stack:
            self.enqueue(stack.pop())
        

q = Queue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.reverse_recursion()
q.reverse_iteration()

while not q.empty():
    print(q.dequeue(), end=" ")
