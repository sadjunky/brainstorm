

def push(ele):
    lqueue.insert(0, ele)

def pop():
    while lqueue:
        ele = lqueue.pop()
        rqueue.append(ele)
        for i in range(len(rqueue) - 1):
            ele = rqueue.pop(0)
            rqueue.append(ele)
    return rqueue.pop(0)

lqueue = []
rqueue = []

push(1)
push(2)
push(3)
print(pop())
push(4)
print(pop())

