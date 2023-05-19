import os
import time


def change_id(li, sace_path):
    car_dic = {}  # 数据类型 int
    ff = open(save_path, 'w')
    num = 0
    for i in li:
        f = open(i, 'r').readlines()
        for i, k in enumerate(f):
            car = k.split(',')
            if int(car[0]) in car_dic:
                car_dic[int(car[0])] = car_dic[int(car[0])] + 1
            else:
                car_dic[int(car[0])] = 0

            car_id = int(car[0]) + 10000000000 * car_dic[int(car[0])]

            ii = f''.join(f'{k},' for k in car[1:])
            ii = str(car_id) + ',' + ii[:-1]
            ff.write(f'{ii}')
            num += 1
    print(num)
    ff.close()


if __name__ == '__main__':
    li = ['/data/WorkMind/data/student/d/one_hour/od_67.txt',
          '/data/WorkMind/data/student/d/one_hour/od_78.txt',
          '/data/WorkMind/data/student/d/one_hour/od_910.txt']

    save_path = '/data/WorkMind/data/student/d/one_hour/od_519.txt'

    change_id(li, save_path)
    # change_id(p2, s2)
    # change_id(p3, s3)

