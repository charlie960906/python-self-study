# 創建字典的字面量語法
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
# 創建字典的構造器語法
items1 = dict(one=1, two=2, three=3, four=4)
# 通過zip函數將兩個序列壓成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 創建字典的推導式語法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通過键可以獲取字典中對應的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 對字典中所有键值對進行遍歷
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通過键獲取對應的值但是可以設置默認值
print(scores.get('武则天', 60))
# 刪除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)