"""
比較運算子&邏輯運算子練習
"""

flag0 = 1 == 1 #1=1 True
flag1 = 3 > 2  # 3>2 True
flag2 = 2 < 1  # 2不小於1 Fause
flag3 = flag1 and flag2 # 兩個都是True才是True
flag4 = flag1 or flag2  # 其中一個是True就是True
flag5 = not (1 != 2)    # 雙重否定 Fause Fause=True

print('flag0=',flag0)
print('flag1=',flag1)
print('flag2=',flag2)
print('flag3=',flag3)
print('flag4=',flag4)
print('flag5=',flag5)