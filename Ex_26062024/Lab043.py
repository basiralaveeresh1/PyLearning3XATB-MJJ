class Dog1:
    name = None
    id = None
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def sleep(self):
        print(f"Who is sleeping -->  {self.name}")


d1 = Dog1("Veeresh",1026)
d2 = Dog1("Yesh", 1027)

d1.sleep()
d2.sleep()

