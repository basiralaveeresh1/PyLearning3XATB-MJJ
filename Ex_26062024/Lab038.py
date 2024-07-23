class Dog:
    name = None
    id = None

    # Constructor ?
    # Use to initialize the values of the instance variables
    def sleep(self):
        print("I can sleep")


dog1 = Dog()
dog1.name = "Tom"
dog1.id = 1206
print(dog1.name)
print(dog1.id)
dog1.sleep()