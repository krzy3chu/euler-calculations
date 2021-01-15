def factorial(value):
    silnia = 1
    for i in range(1, value+1):
        silnia *= i
    return silnia

def euler_from_series(precision):
    euler = 1
    for i in range(1, precision+1):
        euler += 1/factorial(i)
    return euler

print(factorial(0))
print(factorial(5))
print(factorial(8))
print(euler_from_series(1))
print(euler_from_series(2))
print(euler_from_series(3))
print(euler_from_series(4))
print(euler_from_series(100))