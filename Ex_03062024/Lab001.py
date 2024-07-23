print("Welcome to Python")

a = 20
b = 30
a,b = b,a
print("A value:", a)
print("B values:",b)

temp1 = a,b
print(a)
print(b)
print("Method 3rd type:")

x = 5
y = 10
temp2 = x # temp2 = 5
x = y  # x = 10
y = temp2 # y = 5
print("Value of X is: ",x)
print("Value of Y is: ",y)
