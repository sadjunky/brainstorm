
stack = []

arr = [13, 7, 6, 12, 8, 9]

stack.append(arr[0])

for i in range(1, len(arr)):
    while len(stack) and stack[-1] < arr[i]:
        temp = stack.pop()
        print(temp, "->", arr[i])
    stack.append(arr[i])

while len(stack):
    print(stack.pop(), "->", "-1")
