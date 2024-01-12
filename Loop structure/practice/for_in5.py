"""
求1到100的偶數和加入ifelse
"""

sum=0
for i in range(1,101):
    if i%2== 0:
        sum+=i
print(sum)