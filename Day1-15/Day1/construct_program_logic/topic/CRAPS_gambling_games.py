"""
CRAPS賭博遊戲
設定玩家开始遊戲時有1000元的赌注
遊戲结束的条件是玩家输光所有的赌注
"""

from random import randint

money=1000
while money>0:
    print(f'你的總資產為:{money}')
    needs_go_on=False
    while True:
        dept = int(input('請下注:'))
        if 0<dept <=money:
            break