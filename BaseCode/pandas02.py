import pandas as pd


def create_data_frame():
    data = {
        "name": ["yahoo", "google", "facebook"],
        "marks": [200, 400, 800],
        "price": [9, 3, 7]
    }

    dt1 = pd.DataFrame(data)
    print(dt1)

    # 规定columns的顺序
    dt2 = pd.DataFrame(data, columns=['name', 'price', 'marks'])
    print(dt2)

    # 规定索引
    dt3 = pd.DataFrame(data, columns=['name', 'price', 'marks', 'debt'], index=['a', 'b', 'c'])
    print(dt3)

    # 字典套字典
    new_data = {
        "lang": {
            "firstline": "python",
            "secondline": "java"
        },
        "price": {
            "firstline": 8000
        }
    }

    dt4 = pd.DataFrame(new_data)
    print(dt4)

    dt5 = pd.DataFrame(new_data, index=['firstline', 'secondline', 'thirdline'])
    print(dt5)
    print(dt5.columns)
    print(dt5['price'])
    dt5['price'] = 888
    print(dt5)

    sdebt = pd.Series([2.2, 3.3], index=["a", "c"])
    dt5['sdebt'] = sdebt
    print(dt5)

    dt5['sdebt']['firstline'] = 999
    print(dt5)


if __name__ == '__main__':
    create_data_frame()
