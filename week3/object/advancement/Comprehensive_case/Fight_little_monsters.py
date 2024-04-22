from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """戰鬥者"""

    # 透過__slots__魔法限定物件可以綁定的成員變數
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """初始化方法
        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻擊

        :param other: 對象
        """
        pass


class attactor(Fighter):
    """挑戰者"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """初始化方法

        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """必殺技(打掉對方至少50點或3/4的血)

        :param other:被攻擊對象

        :return: 使用成功返回True否則返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击

        :param others: 被攻擊的群體

        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢復魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s挑戰者~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


class Monster(Fighter):
    """小怪獸"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪獸~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    """判斷有没有小怪獸是活著的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """選中一隻活着的小怪獸"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """顯示挑戰者和小怪獸的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = attactor('黃宥鈞',1000, 120)
    m1 = Monster('惡狼', 250)
    m2 = Monster('鳳凰男', 500)
    m3 = Monster('怪人王', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一隻小怪獸
        skill = randint(1, 10)   # 通過隨機選擇使用哪種技能
        if skill <= 6:  # 60%的概率使用普通攻擊
            print('%s使用普通攻擊打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢復了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻擊(可能因魔法值不足而失敗)
            if u.magic_attack(ms):
                print('%s使用了魔法攻擊.' % u.name)
            else:
                print('%s使用魔法失敗.' % u.name)
        else:  # 10%的概率使用必殺技(如果魔法值不足則使用普通攻擊)
            if u.huge_attack(m):
                print('%s使用必殺技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻擊打了%s.' % (u.name, m.name))
                print('%s的魔法值恢復了%d點.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果選中的小怪獸没有死就回擊追中者
            print('%s回擊了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每個回合结束后顯示追中者和小怪獸的信息
        fight_round += 1
    print('\n========戰鬥结束!========\n')
    if u.alive > 0:
        print('%s挑戰者勝利!' % u.name)
    else:
        print('小怪獸勝利!')


if __name__ == '__main__':
    main()