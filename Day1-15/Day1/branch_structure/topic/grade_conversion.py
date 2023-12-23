"""
成績等第換算
要求:如果輸入的成績在90分以上(含90分)輸出A 
                    80分-90分(含90分)輸出B
                    70分-80分(含80分)輸出C
                    60分-70分(含70分)輸出D
                    60分以下輸出E。
"""

score=int(input('請輸入成績:'))

if 100>=score>=0:
    if score >=90:
        grade='A'
    elif score>=80:
        grade='B'
    elif score>=70:
        grade='C'
    elif score>=60:
        grade='D'
    elif score<60:
        grade='E'
    print(f'對應等級是:{grade}')
else:
    print("請輸入有效數字")