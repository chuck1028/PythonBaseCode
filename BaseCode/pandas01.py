import pandas as pd


# 只包含数字
def number_series():
    data = [9, 3, 8]

    ps = pd.Series(data)

    print(ps)


# 混合数据类型
def mix_series():
    data = [100, 'Python', 'AAA', 'BBB']

    ps = pd.Series(data, index=['i', 'ii', 'iii', 'iiii'])

    # print(ps.index)
    # print(ps.values)
    print(ps['i'])
    print(ps['ii'])
    print(ps['iii'])
    print(ps['iiii'])


# 字典创建Series
def dict_series():
    data = {
        '1': 'AAA',
        '2': 'BBB',
        '3': 'CCC',
        '4': 'DDD',
    }

    ps = pd.Series(data)

    print(ps)


# Series自动对齐
def auto_align():
    data = {
        '1': 'AAA',
        '2': 'BBB',
        '3': 'CCC',
        '4': 'DDD',
    }

    ps = pd.Series(data, index=['1', 'python', 'c++', 'c'])
    ps.index = ['a', 'b', 'c', 'd']

    print(ps)
    print(ps.isnull())    # 判断空值


def series_operation():
    data1 = [1, 2, 3, 4]
    data2 = [5, 6, 7, 8]

    ps1 = pd.Series(data1)
    ps2 = pd.Series(data2)

    ps3 = ps1 + ps2
    ps4 = ps1 - ps2
    ps5 = ps1 * ps2
    ps6 = ps1 / ps2

    ps7 = ps2[ps2 > 5]

    print(ps3)
    print(ps4)
    print(ps5)
    print(ps6)
    print(ps7)


if __name__ == '__main__':
    # number_series()
    # mix_series()
    # dict_series()
    # auto_align()
    series_operation()
