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
        print("I am callinig this method when m=object is created")

    # def password_change(self):
    #     self.password = 321
    #     print(self.password)


car1 = Car()
car1.password = 987
print(car1.password)