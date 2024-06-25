# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Examples:
#Convert the tuple into a list to be able to change it:

my_tuple = (4,4, 2, 3, 1)
my_list = list(my_tuple)
print(my_list)
my_list.append(10)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)