"""
質數判斷
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是質數')
else:
    print(f'{num}不是質數')


