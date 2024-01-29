from random import randint

def roll_dice(n=2): #默認2
    total = 0
    for _ in range(n):
        total +=randint(1,6)
    return total


print(roll_dice()) #默認2 搖2次骰子
print(roll_dice(3)) #給予3 搖三次骰子