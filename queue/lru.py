# Calculate number of page faults using LRU page replacement algorithm.
from collections import deque

class LRUCache:
    
    def __init__(self, size) -> None:
        self.deque = deque(maxlen=size) # Doubly ended linked list 
        self.pf = 0
        self.hash = {} # To allow search of elements in O(1) time in the doubly ended linked list 
    
    def __pf_incr(self) -> None:
        self.pf += 1 # Increment page fault for every cache miss
    
    def display(self) -> None:
        return self.pf
    
    def refer(self, value) -> None:
        if value in self.hash:
            self.deque.remove(value)
            print("CACHE HIT!")
        
        elif len(self.deque) == self.deque.maxlen:
            self.hash.pop(self.deque.pop())
            self.hash[value] = 0
            print("CACHE MISS!")
            self.__pf_incr()
        
        else:
            self.hash[value] = 0
            print("CACHE MISS!")
            self.__pf_incr()
        
        self.deque.appendleft(value)


cache = LRUCache(3)
cache.refer(1)
cache.refer(2)
cache.refer(3)
cache.refer(1)
cache.refer(2)
cache.refer(3)
cache.refer(4)
cache.refer(1)
cache.refer(2)
cache.refer(2)
cache.refer(3)
print(cache.display())
