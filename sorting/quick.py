
def quicksort(li, l, r):
    if r - l <= 1:
        return
    
    yellow = l + 1
    for green in range(l+1, len(li)):
        if li[green] <= li[l]:
            li[yellow], li[green] = li[green], li[yellow]
            yellow += 1
    
    li[l], li[yellow - 1] = li[yellow - 1], li[l]

    quicksort(li, l, yellow - 1)
    quicksort(li, yellow, r)

li = [43, 32, 22, 78, 63, 57, 91, 13]
quicksort(li, 0, 7)
print(li)
