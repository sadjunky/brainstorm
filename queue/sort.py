# Sort queue in O(1) space
class Queue:

    def __init__(self) -> None:
        self.queue = []

    def put(self, data) -> None:
        self.queue.append(data)

    def get(self) -> int:
       return self.queue.pop(0)
    
    def sort(self) -> list:
        N = len(self.queue)
        
        for _ in range(len(self.queue)): # Find min element and enqueue to the queue
            min = float('inf')
            min_index = -1

            for j in range(len(self.queue)): # Find minimum element and its index
                temp = self.get()
                if temp < min and j < N:
                    min = temp
                    min_index = j
                self.put(temp)
            
            for j in range(len(self.queue)): # Dequeue and enqueue all elements except the min element
                temp = self.get()
                if j != min_index:
                    self.put(temp)
            
            self.put(min) # Enqueue min element
            N -= 1 # Decrement search space for minimum element 
        
        return self.queue


q = Queue()
q.put(11)
q.put(5)
q.put(4)
q.put(21)
print(q.sort())
