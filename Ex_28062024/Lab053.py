class Myclass:

    def __init__(self):
        self.name = "Veeresh"

    def public_fun(self):
        print("Public fun()")

    def __Private_fun(self):
        print("Private fun()")

    def public_fun_calling_private(self):
        self.__Private_fun()
        print("Public fun calling private fun")
# Security : 
m1 = Myclass()
m1.public_fun_calling_private()
#m1.public_fun()