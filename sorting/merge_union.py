
def merge(L, R):
    C, m, n = [], len(L), len(R)
    i, j = 0, 0

    while i+j < m+n:
        if i == m:
            C.append(R[j])
            j += 1
        elif j == n:
            C.append(L[i])
            i += 1
        elif L[i] < R[j]:
            C.append(L[i])
            i += 1
        elif L[i] > R[j]:
            C.append(R[j])
            j += 1
        else:
            C.append(L[i])
            i += 1
            j += 1
    return C

def sort(li, left, right):
    if right - left <= 1:
        return li[left:right]
    
    mid = (left + right) // 2
    L = sort(li, left, mid)
    R = sort(li, mid, right)

    return merge(L, R)

li = [2, 3, 1, 3, 5, 7, 7, 9]
print(sort(li, 0, len(li)))
