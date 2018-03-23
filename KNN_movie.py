import KNN
import matplotlib.pyplot as plt
import operator
from numpy import *


def create_data():

    # 训练数据
    # [Movie Title]             [number of FightScene]    [number of KissScene]     [Type]
    # California Man                      3                       104                LOVE
    # He's Not Realy int Dudes            2                       100                LOVE
    # Beatiful Women                      1                       81                 LOVE
    # Kevin LongBlade                     101                     10                 ACTION
    # Robo Slayer 3000                    99                      5                  ACTION
    # Amped 2                             98                      2                  ACTION
    # ?                                   18                      90                <UNKNOWN>

    group = array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['LOVE', 'LOVE', 'LOVE', 'ACTION', 'ACTION', 'ACTION']
    return group, labels


def demo():
    group, labels = create_data()
    # [[3 104]
    #  [2 100]
    #  [1 81]
    #  [101 10]
    #  [99 5]
    #  [98 2]]
    # print(group)
    # ['LOVE', 'LOVE', 'LOVE', 'ACTION', 'ACTION', 'ACTION']
    # print(labels)

    # 使用模型
    title = input("请输入电影的名字")
    number_of_fight_scene = int(input("请输入打斗场面的镜头数(0-1000)"))
    number_of_kiss_scene = int(input("请输入亲吻场面的镜头数(0-1000)"))
    show_figure([number_of_fight_scene, number_of_kiss_scene], group)
    predicate = classify([number_of_fight_scene, number_of_kiss_scene], group, labels, 3)
    print('%s 的类型为 %s' % (title, predicate))


def show_figure(inX, dataSet):
    # 输入数据的分布状况
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(dataSet[:, 0][0:3], dataSet[:, 1][0:3], c='r', marker='o')
    ax.scatter(dataSet[:, 0][3:6], dataSet[:, 1][3:6], c='g', marker='o')
    ax.scatter(inX[0], inX[1], c='b', marker='o')
    plt.xlabel('fightscene')
    plt.ylabel('kissscene')
    plt.title('KNN')
    plt.show()


def classify(inX, dataSet, labels, k):
    # KNN的主要实现方法
    # 下面的求距离过程就是按照欧氏距离的公式计算的。
    # 即 根号(x^2+y^2)

    # [50, 60]
    print(inX)
    # 获取训练样本的大小
    dataSetSize = dataSet.shape[0]
    # tile属于numpy模块下边的函数
    # tile（A, reps）返回一个shape=reps的矩阵，矩阵的每个元素是A
    # 比如 A=[0,1,2] 那么，tile(A, 2)= [0, 1, 2, 0, 1, 2]
    # tile(A,(2,2)) = [[0, 1, 2, 0, 1, 2],
    # [0, 1, 2, 0, 1, 2]]
    # tile(A,(2,1,2)) = [[[0, 1, 2, 0, 1, 2]],
    # [[0, 1, 2, 0, 1, 2]]]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # [[47 - 44]
    #  [48 - 40]
    #  [49 - 21]
    #  [-51 50]
    #  [-49 55]
    #  [-48  58]]
    print(diffMat)
    sqDiffMat = diffMat ** 2
    # [[2209 1936]
    #  [2304 1600]
    #  [2401 441]
    #  [2601 2500]
    #  [2401 3025]
    #  [2304 3364]]
    print(sqDiffMat)
    # axis=1表示按照横轴，sum表示累加，即按照行进行累加。
    sqDistances = sqDiffMat.sum(axis=1)
    # [4145 3904 2842 5101 5426 5668]
    print(sqDistances)
    distances = sqDistances ** 0.5
    # [64.38167441 62.48199741 53.31041174 71.42128534 73.66138744 75.2861209 ]
    print(distances)
    # 按照升序进行快速排序，返回的是原数组的下标。
    # 比如，x = [30, 10, 20, 40]
    # 升序排序后应该是[10,20,30,40],他们的原下标是[1,2,0,3]
    # 那么，numpy.argsort(x) = [1, 2, 0, 3]
    sortedDistIndicies = distances.argsort()
    # [2 1 0 3 4 5]
    print(sortedDistIndicies)

    # 存放最终的分类结果及相应的结果投票数
    classCount = {}
    for i in range(k):
        print(sortedDistIndicies[i])
        voteIlabel = labels[sortedDistIndicies[i]]
        print(voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        print(classCount)
        # 投票过程，就是统计前k个最近的样本所属类别包含的样本个数
        # 2
        # LOVE
        # {'LOVE': 1}
        # 1
        # LOVE
        # {'LOVE': 2}
        # 0
        # LOVE
        # {'LOVE': 3}
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 把分类结果进行排序，然后返回得票数最多的分类结果
    # [('LOVE', 3)]
    print(sortedClassCount)
    return sortedClassCount[0][0]


if __name__ == '__main__':
    demo()
