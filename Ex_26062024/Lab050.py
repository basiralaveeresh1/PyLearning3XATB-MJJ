class VWOLoginPageOne:

    email = None
    password = None

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def display_login_details(self):
        if self.email == "bvs@yopmail.com" and self.password == "Test@123":
            print("Login Successful")
        else:
            print("Login Failed")

email = input("Enter the email: \n")
password = input("Enter the password: \n")

obj1 = VWOLoginPageOne(email, password)
obj1.display_login_details()
