"""
費氏數列
兔子問題
"""

def fibonacci(x):  #費氏數列                               
    if x==0: return 0
    elif x==1 or x==2: return 1
    else : return fibonacci(x-1)+fibonacci(x-2)

x=int(input('想要知道幾個月後呢:'))
print(fibonacci(x))