import os
import time


def rm_wrong():
    path = '/data/WorkMind/data/student/d/FilterData_1.txt'
    save_path = '/data/WorkMind/data/student/d/Save_data.txt'
    f = open(path, 'r').readlines()
    num = 0
    # id = '8617292022147'
    ff = open(save_path, 'w')
    for i in f:
        num += 1
        car = i.split(',')
        if len(car) == 7 and car[3] in ['0', '-1']:
            ff.write(i)


def take_one_hour():
    path = '/data/WorkMind/data/student/d/Save_data.txt'
    save_path = '/data/WorkMind/data/student/d/7_8.txt'

    f = open(path, 'r').readlines()
    num = 0
    # id = '8617292022147'
    ff = open(save_path, 'w')
    for i in f:
        car = i.split(',')
        if 1569236400 <= int(car[6]) <= 1569240000:
            ff.write(i)
            num += 1
    print(num)


def t():
    print(time.time())
    # ti = time.time()
    ten_timeArray = time.localtime(1569168001)
    ten_otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray)
    print('ten_otherStyleTime', ten_otherStyleTime)


def make_data():
    path = '/data/WorkMind/data/student/d/7_8.txt'
    save_path = '/data/WorkMind/data/student/d/78time.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    for i in f:
        car = i.split(',')
        ten_timeArray = time.localtime(int(car[6]))
        ten_otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray)
        car[6] = ten_otherStyleTime
        ii = ''.join(f'{k},' for k in car)
        ii = ii[:-1]
        ff.write(f'{ii}\n')


def make_use():
    path = '/data/WorkMind/data/student/d/78time.txt'
    save_path = '/data/WorkMind/data/student/d/78use.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    for i, k in enumerate(f):
        car = k.split(',')
        for ii, j in enumerate(f[i + 1:]):
            car2 = j.split(',')
            if car[0] == car2[0] and car[3] != car2[3]:
                for h in f[ii + 1:]:
                    car3 = h.split(',')
                    if car[0] == car2[0] and car[3] != car3[3]:
                        print(i)
                        pass

        # print(ii)
        # ff.write(f'{ii}\n')


def make_use2():
    path = '/data/WorkMind/data/student/d/78time.txt'
    save_path = '/data/WorkMind/data/student/d/78use.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    num = 0
    for i, k in enumerate(f):
        if num < 100:
            car = k.split(',')
            if car[3] == '0':  # 此时空车
                for ii, j in enumerate(f[i + 1:]):
                    car2 = j.split(',')
                    if car[0] == car2[0] and car2[3] == '-1':  # 此时上车
                        for h in f[ii + 1:]:
                            car3 = h.split(',')
                            if car[0] == car3[0] and car3[3] == '0':  # 此时下车
                                # print(k, j, h)
                                ff.write(k)
                                ff.write(j)
                                ff.write(h)
                                ff.write('\n')
                                num += 1
                                break
                        break


def make_use3():  # 连续筛选四条信息
    path = '/data/WorkMind/data/student/d/78time.txt'
    save_path = '/data/WorkMind/data/student/d/78use2.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    num = 0
    for i, k in enumerate(f):
        if num < 10:
            car = k.split(',')
            # if car[3] == '0':  # 此时空车
            for ii, j in enumerate(f[i + 1:]):
                car2 = j.split(',')
                if car[0] == car2[0] and car2[3] != car[3]:  # 此时上车
                    for iii, h in enumerate(f[i + ii + 1:]):
                        car3 = h.split(',')
                        if car[0] == car3[0] and car3[3] != car2[3]:  # 此时下车
                            for iiii, g in enumerate(f[i + ii + iii + 1:]):
                                car4 = g.split(',')
                                if car[0] == car4[0] and car4[3] != car3[3]:
                                    # car = i.split(',')

                                    # print(k, j, h, g)
                                    # ff.write(k)
                                    # ff.write(j)
                                    # ff.write(h)
                                    # ff.write(g)
                                    # ff.write('\n')
                                    # num += 1
                                    break
                            break
                    break


def make_all_od():
    path = '/data/WorkMind/data/student/d/7_8.txt'
    save_path = '/data/WorkMind/data/student/d/all_od.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    num = 0
    for i, k in enumerate(f):
        # if num < 10:
        car = k.split(',')
        if car[3] == '0' and i + 1 < len(f):  # 此时空车
            for ii, j in enumerate(f[i + 1:]):
                car2 = j.split(',')
                if car[0] == car2[0] and car2[3] != car[3] and i + ii + 2 < len(f):  # 此时上车
                    for iii, h in enumerate(f[i + ii + 2:]):
                        car3 = h.split(',')
                        if car[0] == car3[0] and car3[3] != car2[3] and i + ii + iii < len(f):  # 此时下车
                            for iiii, g in enumerate(f[i + ii + iii + 3:]):
                                car4 = g.split(',')
                                if car[0] == car4[0] and car4[3] != car3[3] and (int(car3[6]) - int(car[6])) > 300:
                                    ten_timeArray_1 = time.localtime(int(car[6]))
                                    ten_otherStyleTime_1 = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray_1)

                                    ten_timeArray_2 = time.localtime(int(car3[6]))
                                    ten_otherStyleTime_2 = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray_2)

                                    od = ''
                                    od += car2[0]
                                    od += ','
                                    od += ten_otherStyleTime_1
                                    od += ','
                                    od += car2[1]
                                    od += ','
                                    od += car2[2]
                                    od += ','
                                    od += ten_otherStyleTime_2
                                    od += ','
                                    od += car4[1]
                                    od += ','
                                    od += car4[2]
                                    print(od, num)
                                    ff.write(f'{od}\n')
                                    num += 1

                                    break
                            break
                    break
    print('统计完成，总共：', num)


def make_all_od_4():
    path = '/data/WorkMind/data/student/d/7_8.txt'
    save_path = '/data/WorkMind/data/student/d/all_od_4.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    num = 0
    car_list = []  # 汽车列表
    for i, k in enumerate(f):
        # if num < 10:
        car = k.split(',')
        if i + 1 >= len(f):
            break
        if car[3] == '0' and (car[0] not in car_list):  # 此时空车  一辆车只要一次  状态是0
            car_list.append(car[0])
            for ii, j in enumerate(f[i + 1:]):
                car2 = j.split(',')
                if i + ii + 2 >= len(f):
                    break
                if car[0] == car2[0] and car2[3] != car[3]:
                    # 此时上车    状态是-1 载客了，这个时候比较重要,如果下面的不符合直接break   一旦开始载客，就要一直找到下车的时候
                    for iii, h in enumerate(f[i + ii + 2:]):
                        car3 = h.split(',')
                        if car[0] == car3[0] and car3[3] != car2[3]:  # 此时下车了，状态是空车，下面无论怎么执行都要break
                            if int(car3[6]) - int(car2[6]) > 300:
                                timeArray_1 = time.localtime(int(car2[6]))  # 上车的时间
                                otherStyleTime_1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_1)
                                timeArray_2 = time.localtime(int(car3[6]))  # 下车的时间
                                otherStyleTime_2 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_2)

                                od = ''
                                od += car2[0]
                                od += ','
                                od += otherStyleTime_1
                                od += ','
                                od += car2[1]
                                od += ','
                                od += car2[2]
                                od += ','
                                od += otherStyleTime_2
                                od += ','
                                od += car3[1]
                                od += ','
                                od += car3[2]
                                print(od, num)
                                ff.write(f'{od}\n')
                                num += 1
                            else:
                                break  # 这个是
                            break  # 检测到下车
                    break  # 检测到上车
    print('统计完成，总共：', num)


if __name__ == '__main__':
    # r_c()
    # t()
    # take_new_5000()
    # make_data()
    # make_use()
    # make_use2()
    # make_use3()
    # make_all_od()
    make_all_od_4()
