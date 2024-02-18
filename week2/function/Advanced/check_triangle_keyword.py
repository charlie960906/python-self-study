def check_triangle(*, a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b

#傳送時必須使用"參數名=參數值"
print(check_triangle(a=3, b=4, c=5))
print(check_triangle(c=5, b=4, a=3))