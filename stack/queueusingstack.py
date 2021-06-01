

def push(ele):
    if not len(rstack):
        rstack.append(ele) 
    else:
        temp = rstack.pop()
        push(ele)
        rstack.append(temp)


def dequeue():
    if not len(rstack) and len(lstack):
        while len(lstack):
            temp = lstack.pop()
            rstack.append(temp)
    elif len(lstack):
        ele = lstack.pop()
        push(ele)
    else:
        return "Queue is empty!"
    return rstack.pop()


def enqueue(ele):
    lstack.append(ele)

lstack = []
rstack = []

enqueue(1)
enqueue(2)
enqueue(3)
print(dequeue())
enqueue(4)
print(dequeue())
