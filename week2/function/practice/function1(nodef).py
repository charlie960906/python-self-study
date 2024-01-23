m = int(input('m = '))
n = int(input('n = '))
# 計算m的階乘
fm = 1
for num in range (1,m+1):
    fm *= num
# 計算n的階乘
fn =1
for num in range(1,n+1):
    fn *=num
# 計算m-n的階乘
fk =1
for num in range(1,m-n+1):
    fk*= num
#計算C(M,N)的值
print(fm// fn // fk)