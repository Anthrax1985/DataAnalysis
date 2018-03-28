# 财富游戏、真实社会中有100人
# 每人每轮要在游戏中给随机一个人1块钱
# 观察财富所得

import matplotlib.pyplot as plt
import matplotlib
import random
import time
import imp

_init_money = 100
_total = 100
_peoples = [_init_money for i in range(1, _total+1)]
_people_earn_count = [0 for i in range(1, _total+1)]
_round = 0
_round_number = 20000
# matplotlib.interactive(True)
# imp.reload(matplotlib)
_fig = plt.figure()

def start_game(num):
    print("当前轮数:%s" % _round)
    for i in range(1, num+1):
        plt.title(i)
        give_money_to_other()


def give_money_to_other():
    for i in range(100):
        earn_people = random.randint(1, 100)
        _people_earn_count[earn_people - 1] += 1
        print('第%d个人的钱随机分给第%d个人' % (i, earn_people))
        _peoples[i] -= 1
        _peoples[earn_people -1] += 1



def refresh_data():
    x = [i for i in range(_total)]
    # y = sorted([_peoples[i] for i in range(_total)])
    y = [_peoples[i] for i in range(_total)]
    plt.bar(x, y)
    plt.show()


if __name__ == '__main__':
    print('Game Start！')

    start_game(_round_number)
    print(_people_earn_count)
    print(_peoples)
    refresh_data()
    print(max(_peoples))
    print(min(_people_earn_count))