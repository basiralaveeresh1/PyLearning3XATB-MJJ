def fun1():
    print("Hello")


fun1()

# Without
def fun2(a):
    print(a)


fun2(10)


def fun3(b,c):
    return b+c


print(fun3(c=5,b=6))


def fun4(name):
    return f"Hello,{name}"


name = fun4("Veeresh")
print(name)

def print_info(name,age):
    return f"Name: {name}, Age: {age} "

print(print_info("Veeresh",34))

# Default Arguments

def fun5(name="Veeresh Basirala"):
    print(name)
    print(f"Hellow: {name}")


fun5()
fun5("Swetha")