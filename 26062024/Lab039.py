class Person:
    name = None
    id = None
    age = None
    phone_no = None
    def talk(self):  # Method -- If we declare with in the class we can call it as a Method
        print("I can talk")
    def walk(self): # Method
        print("I can walk")
    def eat(self): # Method
        print("I can eat")

def another(): # Function -- If the we declare outside the class. We can call it as a Function
    print("This is another function")

person_details = Person() # Object creation

person_details.name = "Veeresh" # Assigning the values to the variables
person_details.id = 1206 # Assigning the values to the variables
person_details.age = 32 # Assigning the values to the variables
person_details.phone_no = 9845012345 # Assigning the values to the variables

print(person_details.name) # Printing the values
print(person_details.id) # Printing the values
print(person_details.age) # Printing the values
print(person_details.phone_no) # Printing the values

person_details.talk() # Calling the Method
person_details.walk() # Calling the Method
person_details.eat() # Calling the Method
another() # Calling the Function