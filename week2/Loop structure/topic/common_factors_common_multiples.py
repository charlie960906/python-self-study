"""
找最小公因數和最大公倍數
"""

x=int(input('x='))
y=int(input('y='))
#如果x>y就交換x and y的值

if x>y:
    x,y=y,x
#從兩個數開始做遞減循環
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor ==0:
        print(f'{x}and{y}的最大公因數是{factor}')
        print(f'{x}and{y}的最小公倍數是{x*y}')
        break