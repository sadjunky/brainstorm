
def delete(li, index):
    n = len(li)
    if index == n - 1:
        return li[0:index]

    for i in range(index, len(li)):
        if i == n - 1:
            break
        li[i] = li[i + 1]
    n -= 1
    return li[0:n]

print(delete([1, 2, 3, 4, 5], 0))



