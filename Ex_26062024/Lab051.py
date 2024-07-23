# Encapsulation
# bind the data variables and methods
# Data Member / CLass Variable
# Methods - Def function within the class
# Wrapping or binding the data variables with the methods

# Hide the data members (class vaiables, instance variable) by using only the methods

class Car:
    name = None
    password = 123

    def __init__(self):
        self.public_var = "public"
        self.__private_var = "private"
        self._protected_var = "protected"


    def __private_method(self):
        print("Inside Private Method")


    def public_method(self):
        print("Inside Public Method")
        print(self.__private_var)
        print(self._protected_var)
        print(self.public_var)
        self.__private_method()

car1 = Car()
# car1.password = 987
# print(car1.password)
# print(car1.password_change())

car1.public_method()
