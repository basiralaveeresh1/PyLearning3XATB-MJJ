class Person:
    # Class variable or Instance variable
    name = "Veeru"
    age = None

    def display(self):
        a = 20 # Local variable
        print("I am method")
        print("Hi", self.age)


object_reference = Person()
object_reference.display()