x = "hot"
y = "dog"
list1 = x.split()
list3 = [i for i in x]
list2= []
# print(list1)
for i in list1[0]:
    list2.append(i)
print(list3)

#z = [[i] for i in list2 for i in ]
""" z = [[i, j] for i in range(x) for j in range(y) if i + j != 4]
print(z)

x1 = [3, 7, 8]
x2 = [1, 6, 3, 5]

print((x1+x2))
z = [[i] for i in x1 if i in x2]
print(z)

x3 = map(x1 , x2)
print(x3)
"""

