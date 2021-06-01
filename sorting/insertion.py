
def sort(li):
    for i in range(len(li)):
        while i > 0 and li[i] < li[i - 1]:
            li[i], li[i - 1] = li[i - 1], li[i]
            i -= 1
    return li

print(sort([74, 32, 89, 55, 21, 64]))
