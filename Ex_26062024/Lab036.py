# try:
#     number = int(input("Enter the number:"))
#     print(1 / number)
# except ZeroDivisionError:
#     print("You cont division by zero")
# except ValueError:
#     print("Enter only numbers")
# except Exception:
#     print("Something went wrong")
# except ValueError:
#     print("Enter only numbers")

try:
    x = int(input("Enter the number:"))
    print(20/x)
except NameError:
    print("Variable x is not defined")
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Enter only numbers")
except:
    print("Something went wrong")
finally:
    print("This will always be executed")