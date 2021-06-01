
def sort(li):
    for start in range(len(li)):
        min = start
        for i in range(min, len(li)):
            if li[i] < li[min]:
                min = i
        li[start], li[min] = li[min], li[start]
    return li

print(sort([74, 32, 89, 55, 21, 64])) 
