"""
輸入年份判斷是不是閏年
"""

year=int(input('輸入年份:'))

if year %4==0 and year % 100!= 0 or year%400==0:
    print('閏年')
else:
    print('平年')