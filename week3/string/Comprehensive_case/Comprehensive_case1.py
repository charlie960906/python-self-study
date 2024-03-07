from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的雙色球號碼
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    隨機選一組號碼
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('機選幾注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()