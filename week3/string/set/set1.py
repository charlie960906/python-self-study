#創建集合的字面量詞法
set1={1,2,3,3,3,2}
print(set1)
print('Length=',len(set1))
set2=set(range(1,10))
set3=set((1,2,3,3,2,1))
print(set2,set3)
#創建集合的推導式語法(推導式也可以用於推導集合)
set4={num for num in range(1,100) if num % 3 == 0 or num %5==0}
print(set4)

set1.add(4)
set1.add(5)
set2.update([11,12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1,set2)
print(set3.pop())
print(set3)

# 集合的交集、並集、差集、對稱差運算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判斷子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))