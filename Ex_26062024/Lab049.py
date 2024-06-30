# Web Automation Selenium project for sample
class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):

       # self.password = input("Enter the password: ")

        if self.password == "Test@123" and self.email == "bvs@yopmail.com":
            # Login Successful

            print("Login Successful")
        else:
            print("Login Failed")


veeresh = VWOLoginPage("bvs@yopmail.com","Test@123")
yesh = VWOLoginPage("bvs01@yopmail.com", "Test@123")
veeresh.login_confirm()
yesh.login_confirm()
