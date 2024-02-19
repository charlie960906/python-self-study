#def 元組
t =("宥鈞",16,True,'嘉義高中')
print(t)
#獲取元組中的元素
print(t[0])
print(t[3])
#遍歷元組中的值
for member in t:
    print(member)
#重新給元組賦值
#t[0]  '黃小鈞' #TypeError
#變量t重新引用了新的元組原來的元組將被垃圾回收
t=('黃小鈞',20,True,'臺灣嘉義')
print(t)
#轉成列表
person=list(t)
print(person)
#列表可以修改元素
person[0]='黃大鈞'
person[1]=25
print(person)
#將列表轉換成元組
fruits_list=['apple','banana','orange']
fruits_tuple=tuple(fruits_list)
print(fruits_tuple)