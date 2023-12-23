"""
英制單位英吋與公制單位公分互換
"""

value=float(input('請輸入長度:'))
unit=input('請輸入單位:')

if unit == '英制':
    print(f'{value}英吋={value*2.54}公分')
elif unit == '公制':
    print(f'{value}公分={value/2.54}英吋')
else:
    print('請輸入有效單位')