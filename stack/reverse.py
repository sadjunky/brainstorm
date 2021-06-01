

def insert(ele, s):
    if len(s) == 0 or ele > s[-1]:
        s.append(ele)
    else:
        temp = s.pop()
        insert(ele, s)
        s.append(temp)


def sort_stack(s):
    if len(s):
        temp = s.pop()
        sort_stack(s)
        insert(temp, s)


stack = []

stack.append(30)
stack.append(-18)
stack.append(40)
stack.append(36)
stack.append(2)

for i in range(len(stack) - 1, -1, -1):
    print(stack[i], end=" ")
print(" ")

sort_stack(stack)

for i in range(len(stack) - 1, -1, -1):
    print(stack[i], end=" ")
print(" ")
