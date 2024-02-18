def check_triangle(a,b,c):
    print(f'a={a},b={b},c={c}')
    return a+b>c and b+c>a and a+c>b

print(check_triangle(1,2,3))
print(check_triangle(a=1,b=2,c=3))
print(check_triangle(c=1,a=2,b=3))
