

def insert(ele, s):
    if not len(s):
        s.append(ele)
    else:
        temp = s.pop()
        insert(ele, s)
        s.append(temp)


def reverse(s):
    if len(s):
        temp = s.pop()
        reverse(s)
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

reverse(stack)

for i in range(len(stack) - 1, -1, -1):
    print(stack[i], end=" ")
print(" ")
