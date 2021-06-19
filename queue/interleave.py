"""
Interleave an even lengthed queue
For e.g.;
Input : 11 12 13 14 15 16 17 18 19 20
Output : 11 16 12 17 13 18 14 19 15 20
"""
def interleave(queue):
    stack = []
    size = len(queue)
    for i in range(size): # push first half of queue to stack
        if i >= (size / 2):
            break
        stack.append(queue.pop())
    while stack: # enqueue stack contents to queue
        queue.insert(0, stack.pop())
    for i in range(size):
        if i >= (size / 2):
            break
        stack.append(queue.pop())
    while stack:
        queue.insert(0, stack.pop())
    for i in range(size):
        if i >= (size / 2):
            break
        stack.append(queue.pop())
    while stack:
        queue.insert(0, stack.pop())
    for i in range(size):
        if i >= (size / 2):
            break
        stack.append(queue.pop())
    for i in range(size): # Enqueue interleaved elements to the stack
        if i >= (size / 2):
            break
        queue.insert(0, queue.pop())
        queue.insert(0, stack.pop())
    
    print(queue)

queue = []
queue.insert(0, 20)
queue.insert(0, 19)
queue.insert(0, 18)
queue.insert(0, 17)
queue.insert(0, 16)
queue.insert(0, 15)
queue.insert(0, 14)
queue.insert(0, 13)
queue.insert(0, 12)
queue.insert(0, 11)

interleave(queue)
