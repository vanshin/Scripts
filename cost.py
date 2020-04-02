# Python 3.7

''' data.csv
1,30000,20200101,20200130
2,30000,20200102,20200131
3,29000,20200103,20200201
'''

import sys
import datetime
import traceback

DATE_FMT = '%Y%m%d'

def load_data():
    '''将数据改为字段并处理时间'''

    datas = []
    header = ['user_id', 'cost', 'start_day', 'end_day']

    # 从文件加载数据
    with open('data.csv', 'r') as f:
        datas = f.readlines()
    datas = [i.strip().split(',') for i in datas]

    # 处理数据
    ret = []
    for i in datas:

        # 将数据处理为字典
        data = {}
        for index, value in enumerate(i):
            data[header[index]] = i[index]

        # 简单的转换一下格式
        try:
            data['start_day'] = datetime.datetime.strptime(data['start_day'], DATE_FMT)
            data['end_day'] = datetime.datetime.strptime(data['end_day'], DATE_FMT)
            data['user_id'] = int(data['user_id'])
            data['cost'] = int(data['cost'])
        except:
            print(f'error data {data}\n {traceback.format_exc()}')
            continue
        ret.append(data)
    return ret



def get_one_cost(data, calc_date):
    '''假设用户购买会员价格存在不同'''

    cost = 0

    # 过期或者未到期不可收取收益
    if calc_date < data['start_day'] or calc_date > data['end_day']:
        return cost

    # 根据购买时长和金额计算单价收益
    days = (data['end_day'] - data['start_day']).days + 1
    income = data['cost'] // days
    rest = data['cost'] % days

    # 根据计算时间判断收益
    cost = income
    if calc_date == data['end_day']:
        cost += rest

    return cost

def main():

    # 校验输入
    if len(sys.argv) != 2:
        print('use as `python3.7 cost.py 20200102`')
        return

    # 转换计算时间格式
    calc_date = sys.argv[1]

    try:
        calc_date = datetime.datetime.strptime(calc_date, DATE_FMT)
    except ValueError:
        print('not correct input date, use like 20200102(%Y%m%d)')
    except:
        print(f'other error {traceback.format_exc()}')

    # 计算
    datas = load_data()
    total = 0

    for i in datas:
        cost = get_one_cost(i, calc_date)
        print(f'use data {i} calc: user {i["user_id"]} {cost}')
        total += cost
    print(f'total {total}')

if __name__ == '__main__':
    main()


