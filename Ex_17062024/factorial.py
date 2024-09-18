import math

n = 5
factorial = 1

# result = math.factorial(5)
# print(result)

for i in range(1,n+1):
    factorial = factorial * i

print(factorial)