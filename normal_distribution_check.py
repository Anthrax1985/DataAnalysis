from numpy import array

import csv



def read_date():
    with open('data/FebHouse.csv', 'r', encoding='GBK') as f:
        reader = csv.reader(f)
        for item in reader:
            yield item[0].split(';')[1]


def ks_check(target):
    print('------------ks-test----------')
    print('targrt: %s' % [a for a in target])




if __name__ == '__main__':
    _arr = read_date()
    ks_check(_arr)


