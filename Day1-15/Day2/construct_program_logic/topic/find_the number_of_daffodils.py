"""
尋找水仙花數
一個3偶，該數字每個位上數字的立方之和恰好等於它本身
"""

for num in range(100,1000):
    low = num%10
    mid = num//10%10
    high= num//100
    if num==low**3+mid**3+high**3:
        print(num)