# Remove the itesm from the list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
# Remove the items from the list
thislist.remove("apple")
print(thislist)
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item.

thislist.pop()
print(thislist)

#The del keyword also removes the specified index:

del thislist[1]
print("Orange is deleted from the list using 'del' keyword: ",thislist)
#The del keyword can also delete the list completely:

#Clear the List
#The clear() method empties the list.

#The list still remains, but it has no content.

thislist.clear()
print(thislist)