
# Next greatest frequency element
def gen_freq():
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

def ngfe():
    gen_freq()
    for i in range(1, len(lst)):
        while len(stack) and freq[stack[-1]] < freq[lst[i]]:
            temp = stack.pop()
            dict[temp] = lst[i]
        stack.append(lst[i])
    for i in stack:
        dict[i] = -1



stack = []
dict = {}
output = []
freq = {}
lst = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
stack.append(lst[0])
ngfe()

for i in lst:
    output.append(dict[i])

print(output)



