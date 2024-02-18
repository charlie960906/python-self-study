list1=[1,3,5,7,100]
print(list1)
list2=['hello']*3
print(list2)
print(len(list1))
print(list1[0])
print(list1[4])
print([-1])
print([-3])
list1[2]=300
print(list1)
for index in range(len(list1)):
    print(list1[index])

for elem in list1:
    print(elem)

for index,elem in enumerate(list1):
    print(index,elem)