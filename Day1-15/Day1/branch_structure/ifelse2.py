"""
分段函數求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""

x= float(input('x='))
if x>1:
    y=3*x-5
elif -1 <= x and x <= 1:
    y=x+2
else:
    y=5*x+3
print(f'{x}={y}')