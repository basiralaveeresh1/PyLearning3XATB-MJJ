class Cal1:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b


obj_ref = Cal1(10, 20) # If you used constructor then you need to give arguments here only

print("Sum of two numbers: ", obj_ref.sum())