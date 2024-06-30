class Student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def display(self):
        print("My Name is: ",self.name)
        print("My Age is: ", self.age)

       # print(f"Name is {self.name} and Age is {self.age}")



studnt1 = Student()
studnt1.display()