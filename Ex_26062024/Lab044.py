class Calc:

    def sum(self,a,b):
        return a+b

    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b
    def mod(self, a, b):
        return a%b

obj_reference = Calc() #If you use function then you need to give arguments in functions like below
print("Sum of two numbers: ",obj_reference.sum(10,2))
print("Sub of two numbers: ", obj_reference.sub(10, 2))
print("Mul of two numbers: ", obj_reference.mul(10, 2))
print("Div of two numbers: ", obj_reference.div(10, 2))
print("Mod of two numbers: ", obj_reference.mod(10, 2))

# or you can reduce the number of lines


