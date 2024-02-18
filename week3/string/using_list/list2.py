list1=[1,3,5,7,100]
list1.append(200)
list1.insert(1,400)
list1+=[1000,2000]
print(list1)
print(len(list1))
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)
list1.clear()
print(list1)