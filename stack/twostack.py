
def push1(ele):
    global len1
    twostack.insert(0, ele)
    len1 += 1

def push2(ele):
    global len2
    twostack.append(ele)
    len2 += 1

def pop1():
    global len1
    if len1:
        len1 -= 1
        return twostack.pop(0)
    return "Stack is empty!"

def pop2():
    global len2
    if len2:
        len2 -= 1
        return twostack.pop()
    return "Stack is empty!"

twostack = []

len1 = 0
len2 = 0

push1(1)
push1(2)
push2(3)
push2(4)
print(pop1())
print(pop2())
print(pop1())
print(pop2())
print(pop1())
print(pop2())
