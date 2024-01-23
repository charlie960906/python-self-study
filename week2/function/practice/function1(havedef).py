'''
輸入M和N計算(M,N)
'''

def fac(num):
    # 求階乘
    result = 1
    for n in range(1,num+1):
        result*= n
    #返回num的階乘(因變量)
    return result


m=int(input('m = '))
n=int(input('n = '))
print(fac(m) // fac(n) // fac(m-n))