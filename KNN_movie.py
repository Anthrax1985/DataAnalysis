import KNN
from matplotlib.pyplot import plot
from numpy import array


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

    group = array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2], [18, 90]])
    labels = ['LOVE', 'LOVE', 'LOVE', 'ACTION', 'ACTION', 'ACTION']
    return group, labels


def demo():
    group, labels = create_data()
    print(group)
    print(labels)

def classify(inX, dataSet, labels, k):


if __name__ == '__main__':
    demo()