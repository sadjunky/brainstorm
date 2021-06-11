def push(ele):
    queue.append(ele)
    for i in range(len(queue) - 1):
        e = queue.pop(0)
        queue.append(e)

def pop():
    if not len(queue):
        return "Stack empty"
    return queue.pop(0)

queue = []

push(1)
push(5)
push(6)
print(pop())
push(8)
print(pop())
