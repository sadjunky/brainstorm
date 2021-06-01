def push(ele):
    queue.insert(0, ele)

def pop():
    if len(queue) == 1:
        return queue.pop()
    elif not len(queue):
        return "Stack is empty!"
    temp = queue.pop()
    ele = pop()
    queue.append(temp)
    return ele

queue = []

push(1)
push(5)
push(6)
print(pop())
push(8)
print(pop())
print(pop())
print(pop())
print(pop())
