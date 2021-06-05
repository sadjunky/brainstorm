

def insert(ele):
    if not len(stack):
        stack.append(ele)
    else:
        temp = stack.pop()
        insert(ele)
        stack.append(temp)



def reverse(stack):
    if len(stack):
        temp = stack.pop()
        reverse(stack)
        insert(temp)


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
