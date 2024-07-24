class VWOLoginPage:

    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.name = name

    def login_confirm(self):
        if self.__email == "bvs@gmail.com" and self.__password == "Test@123":
            print("Login Successful")
        else:
            print("Invalid Credentials")


v1 = VWOLoginPage("bvs1@gmail.com","Test@123","Veeresh")
v1.login_confirm()
print(v1.name)
