
def sort(li, k):
    if k > 1:
        sort(li, k - 1)
        insert(li, k - 1)

def insert(li, k):
    for i in range(len(li)):
        while i > 0 and li[i] < li[i - 1]:
            li[i], li[i - 1] = li[i - 1], li[i]
            i -= 1

li = [74, 32, 89, 55, 21, 64]
sort(li, len(li))
print(li)
