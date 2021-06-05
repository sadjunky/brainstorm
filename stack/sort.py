# Sorts in descending order
def insert(ele):
    if not len(stack) or ele > stack[-1]:
        stack.append(ele)
    else:
        temp = stack.pop()
        insert(ele)
        stack.append(temp)



def sort(stack):
    if len(stack):
        temp = stack.pop()
        sort(stack)
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

sort(stack)

for i in range(len(stack) - 1, -1, -1):
    print(stack[i], end=" ")
print(" ")
