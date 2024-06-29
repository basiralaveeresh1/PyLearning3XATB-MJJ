'''
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets: '''

fruits = ["apple", "banana", "cherry", "pineapple", "mango", "pappaya"]

print(fruits)

# Accessing the elements

print(fruits[1:5])
print(fruits[0])
print(fruits[-1])
print()
for i in fruits:
    print(i)
if "mango" in fruits:
    print("Mango is present")
