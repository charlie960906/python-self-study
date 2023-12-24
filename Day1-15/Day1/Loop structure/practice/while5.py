"""
猜數字遊戲
"""
import random #生成隨機數函式

answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('請輸入:'))
    if number<answer:
        print('大一點')
    elif number>answer:
        print('小一點')
    else:
        print('恭喜你猜對了!')
        break #跳出表停止循環
print(f'你總共猜了{counter}次')
if counter >7:
    print('明顯的你的智力不足猜不太到')