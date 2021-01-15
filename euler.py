def factorial(value):
    silnia = 1
    for i in range(1, value+1):
        silnia = silnia * i
    return silnia

print(factorial(0))
print(factorial(5))
print(factorial(8))