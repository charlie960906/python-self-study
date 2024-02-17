def gcd_and_lcm(x:int,y:int)->int:
    """求最大公因數和最小公倍數"""
    a,b=x,y
    while b%a!=0:
        a,b=b%a,a
    return a,x*y//a


x,y=map(int,input("輸入兩個數字求最大最小公因倍數:").split())
print(gcd_and_lcm(x,y))