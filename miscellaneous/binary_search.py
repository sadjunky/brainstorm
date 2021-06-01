def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while True:
        if arr[l] == arr[r] == x:
            return True
        if r - l == 0 :
            return False
        mid = (l + r) // 2
        if x == arr[mid]:
            return True
        if x > arr[mid]:
            l = mid + 1
        else:
            r = mid

print(binary_search([1, 2, 3, 4, 5], 0))
