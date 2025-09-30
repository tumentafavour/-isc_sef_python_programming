
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f= f * i
    return (f)


n = 5

result = factorial(n)
print(result)