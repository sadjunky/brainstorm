
def merge(L, R):
    C, m, n = [], len(L), len(R)
    i, j = 0, 0

    while i+j < m+n:
        if i == m:
            j += 1
        elif j == n:
            C.append(L[i])
            i += 1
        elif L[i] < R[j]:
            C.append(L[i])
            i += 1
        elif L[i] > R[j]:
            j += 1
        else:
            i += 1
            j += 1
    return C

print(merge([1, 2, 3, 6], [2, 4, 6, 8]))
