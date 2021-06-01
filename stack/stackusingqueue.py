

def push(ele):
    lqueue.insert(0, ele)
    temp = lqueue.pop()
    rqueue.append(temp)
    

def pop():
    if len(rqueue):
        return rqueue.pop()
    return "Stack is empty!"

lqueue = []
rqueue = []

push(1)
push(2)
push(3)
print(pop())
push(4)
print(pop())

