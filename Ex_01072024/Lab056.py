class Encap:
    __a = 10

    def __display1(self):
        print("Private Display1:", self.__a)

    def display2(self):
        print("This is the public method")
        self.__display1()


def hellp():
    print("I am outside the function")


hellp()

obj = Encap()
obj.display2()



