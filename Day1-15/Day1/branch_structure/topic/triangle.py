"""
判斷輸入的邊長能否構成成三角形，如果能則計算出三角形的周長和面積
"""

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

if a+b>c and a+c>b and b+c>a:
    print(f'周長為:{a+b+c}')
    p=(a+b+c)/2
    print(f'面積為{(p*(p-a)*(p-b)*(p*c))**0.5}')
    #透過邊長計算三角形面積公式為海龍公式(https://zh.wikipedia.org/wiki/海龍公式)
else:
    print('不能構成三角形')
