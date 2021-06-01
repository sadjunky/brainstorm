li = [3, 4, 5, 6, 7, 8, 9, 10, 11]

def isprime(num):
    if num == 2:
        return num;
    for i in range(2, num):
        if num % i == 0:
            return 0
    return num

def square(num):
    return num * num


print(list(map(square, filter(isprime, li))))
