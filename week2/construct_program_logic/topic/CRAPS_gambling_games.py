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
        debt = int(input('請下注:'))
        if 0<debt <=money:
            break
    first = randint(1,6)+randint(1,6)
    print(f'玩家搖出了{first}')
    if first == 7 or first==11:
        print('玩家勝!')
        money += debt
    elif first == 2 or first ==3 or first ==12:
        print('莊家勝!')
        money -+ debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1,6)+randint(1,6)
        print(f'玩家搖出了{current}')
        if current ==7:
            print('莊家勝')
            money -= debt
        elif current == first:
            print('玩家勝')
            money += debt
        else:
            needs_go_on = True
print('你破產了,遊戲結束!')