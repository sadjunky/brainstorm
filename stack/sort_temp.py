# Uses a temporary stack to push elements with the smallest at the bottom and the largest at the top of the temporary stack
def push(ele):
    if not len(temp_stack) or ele > temp_stack[-1]: 
        temp_stack.append(ele)
    else:
        temp = temp_stack.pop()
        push(ele)
        temp_stack.append(temp)

def pop(stack):
    if len(stack):
        temp = stack.pop()
        pop(stack)
        push(temp)

def sort(stack):
    pop(stack)
    while len(temp_stack):
        temp = temp_stack.pop()
        stack.append(temp)
        

stack = []
temp_stack = []

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
