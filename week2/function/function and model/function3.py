def add(a=0,b=0,c=0):
    '''三個數相加求和'''
    return a+b+c


print(add()) #都是預設
print(add(1)) #給a
print(add(1,2)) #給a,b
print(add(1,2,3)) #給a,b,c 
print(add(a=2,b=3,c=3))
print(add(c=100,a=100,b=200))