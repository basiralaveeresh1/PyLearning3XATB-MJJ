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
print(fruits[-2])
print("This is new list\n")
list1 = [6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5]
print(list1)
list1.append(12345)
print(list1)

list1.extend(list2)
print(list1)

fruits = ('apple', 'banana', 'cherry')

cars = ['Ford', 'BMW', 'Volvo']

print(fruits)

numbers = (1, 2, 3, 4, 5, 5, 6, 7)
print(numbers[1])

if fruits == "apple":
    print("Apple is present")
else:
    print("Apple is not present")

print("Holllllllllllllll\n")








# Python List index()
# Python List append()  # Add the items to the end of the list (you wanted to add the one item to the list of one list to another list by using append method ()
a = [1,1, 2, 3, 4, 5, "Hari"]
b = (33,33,44,55,66,77)
c = {"Ind","USA","UK"}
# a.append(4)
# print(a)
#
# a.append(b)
# print(a)
# a.extend(b)
# print(a)
a.extend(b)
print(a)

a.extend(c)
print(a)

print(a.count(10))
# Python List extend()
# Python List insert()
# Python List remove()
# Python List count()
# Python List pop()
# Python List reverse()
# Python List sort()
# Python List copy()
# Python List clear()

city = ["Hyderabad","Bangalore","Amaravati"]
print(city.reverse())

# for i in reversed(city):
#     print(i)

city.sort()
print(city)

numbers = [1,40,60,70,3,6,8,25]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

c_list1 = ["A","B","C","D"]

c_list2 = c_list1.copy()

print(c_list2)

c_list2.append("Apple")
print(c_list2)
print(c_list1)










