def sum_three(a=2,b=1,c=1):
    return a+b+c


result1 = sum_three()
result2 = sum_three(a=3,b=4)
print(result1,result2)


lists = ["Mango","Banana","Apple","Orange"]

for i in lists:
    print(i, end=" ")

print("\n")
for j in range(1,10):
    print(j)