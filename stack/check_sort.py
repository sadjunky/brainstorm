



def check_sort(i, o):
    stack.append(i.pop(0))
    while len(i):
        if len(i) == 1:
            o.append(i.pop(0))
            break
        temp = i.pop(0)
        if temp < i[0]:
            o.append(temp)
        elif temp < stack[-1]:
            stack.append(temp)
        else:
            return False
    return True
            


qinput = []
qoutput = []
stack = []

qinput.append(5)
qinput.append(4)
qinput.append(3)

print(check_sort(qinput, qoutput))
