import datetime

start = datetime.datetime.now() #計時

for i in range(1,1000000000000):
    sum=0
    for j in range(1,i):
        if i%j == 0:
            sum+= j
    if sum==i:
        print(i)

end = datetime.datetime.now()
print(f'程式運行了{end-start}秒')