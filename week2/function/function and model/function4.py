#用星號表達args可以接受任意多個參數
def add(*args):
    total=0
    #可變摻數可以放在for迴圈取出每個參數的值
    for val in args:
        if type(val) in (int,float):
            total += val
    return total

#使用add函數並傳入值
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,3,5,7,9))
