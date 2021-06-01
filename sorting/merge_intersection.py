
def merge(L, R):
    C, m, n = [], len(L), len(R)
    i, j = 0, 0

    while i+j < m+n:
        if i == m:
            j += 1
        elif j == n:
            i += 1
        elif L[i] < R[j]:
            i += 1
        elif L[i] > R[j]:
            j += 1
        else:
            C.append(L[i])
            i += 1
            j += 1
    return C

print(merge([1, 3, 5], [2, 3, 4]))
