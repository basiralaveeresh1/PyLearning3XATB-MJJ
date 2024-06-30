class Dog:
    # Constructor ?
    # Use to initialize the values of the instance variables
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def sleep(self):
        print("I can sleep")
        print(self.name)
        print(self.id)


dog1 = Dog("Veeresh",1026)
dog2 = Dog("Yesh", 1027)
dog1.sleep()
dog2.sleep()