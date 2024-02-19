f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表達式語法創建列表容器
# 用這種语法創建列表之後元素已經準備就緒所以需要耗費較多的內存空間
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看對象占用內存字節數
print(f)
# 请注意下面的代碼創建的不是一個列表而是一個生成器對象
# 通過生成器可以獲取到數據但它不占用額外的空間存儲數據
# 每次需要數據的時候就通過內部的運算得到數據(需要花費額外的時間)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存儲數據的空間
print(f)
for val in f:
    print(val)