import time
import numpy as np


def t():
    print(time.time())
    ti = time.time()
    ten_timeArray = time.localtime(1569236449)
    ten_otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray)
    print('ten_otherStyleTime', ten_otherStyleTime)

    ten_timeArray1 = time.localtime(1569236454)
    ten_otherStyleTime1 = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray1)
    print('ten_otherStyleTime', ten_otherStyleTime1)


def cul_time():
    # t_num =
    dt = "2019-09-23 20:00:00"
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    print(timeArray)
    # 3.转为时间戳
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)


def change_time():
    path = '/data/WorkMind/data/student/d/5000_data.txt'
    save_path = '/data/WorkMind/data/student/d/5000.txt'

    f = open(path, 'r').readlines()
    # f = eval(str(f))
    # f = f.readlines()
    num = 0
    id = '8617292022147'
    ff = open(save_path, 'w')
    for i in f:
        car = i.split(',')
        ten_timeArray = time.localtime(int(car[6]))
        ten_otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray)
        car[6] = ten_otherStyleTime

        ii = ''.join(f'{k},' for k in car)
        ii = ii[:-1]

        # print(ii)
        ff.write(f'{ii}\n')
        # num += 1


# ['8617292033583', '115.93354', '40.82624', '0', '0.0', '0.0', '2019-09-23 19:00:49']
# ['8617292033583', '115.93354', '40.82624', '0', '0.0', '0.0', '2019-09-23 19:01:49']

def tes_00():
    l = ['.' * 4 for _ in range(2)]
    print(l)  # 输出：['....', '....']
    print(l[0][2])  # 输出：.

    l[0] = list(l[0])  # 第一步将列表转换成字符串
    print(l)  # 输出：[['.', '.', '.', '.'], '....']

    l[0][2] = 'Q'  # 改变列表中的元素
    print(l)  # 输出：[['.', '.', 'Q', '.'], '....']

    l[0] = ''.join(l[0])  # 将列表转换成字符串
    print(l)  # 输出：['..Q.', '....']


def make_all_od():
    path = '/data/WorkMind/data/student/d/7_8.txt'
    save_path = '/data/WorkMind/data/student/d/one_od.txt'

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
                                if car[0] == car4[0] and car4[3] != car3[3] and (int(car4[6]) - int(car2[6])) > 300:
                                    ten_timeArray_1 = time.localtime(int(car2[6]))
                                    ten_otherStyleTime_1 = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray_1)

                                    ten_timeArray_2 = time.localtime(int(car4[6]))
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
                                    print(od)
                                    ff.write(f'{od}\n')
                                    num += 1

                                    break
                            break
                    break


def make_all_od_2():
    path = '/data/WorkMind/data/student/d/7_8.txt'
    save_path = '/data/WorkMind/data/student/d/all_od_2.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    num = 0
    car_list = []
    for i, k in enumerate(f):
        # if num < 10:
        car = k.split(',')
        if car[3] == '0' and (car[0] not in car_list):  # 此时空车  一辆车只要一次
            car_list.append(car[0])
            for ii, j in enumerate(f[i + 1:]):
                car2 = j.split(',')
                if car[0] == car2[0] and car2[3] != car[3]:  # 此时上车
                    for iii, h in enumerate(f[i + ii + 2:]):
                        car3 = h.split(',')
                        if car[0] == car3[0] and car3[3] == car2[3]:  # 此时还在车上准备下车
                            for iiii, g in enumerate(f[i + ii + iii + 3:]):
                                car4 = g.split(',')
                                if car[0] == car4[0] and car4[3] != car3[3]:  # 此时下车了
                                    if int(car3[6]) - int(car[6]) > 300:
                                        timeArray_1 = time.localtime(int(car2[6]))
                                        otherStyleTime_1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_1)
                                        timeArray_2 = time.localtime(int(car4[6]))
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
                                        od += car4[1]
                                        od += ','
                                        od += car4[2]
                                        print(od, num)
                                        ff.write(f'{od}\n')
                                        num += 1

                                        break
                                    else:
                                        break
                            break
                    break
    print('统计完成，总共：', num)


def cuaclu():
    path = '/data/WorkMind/data/student/d/7_8.txt'
    f = open(path, 'r').readlines()
    print(len(f))
    num = 0


def make_var():
    a = [463, 458, 468, 481, 392, 400, 299, 298, 297, 295]
    b = [1, 2, 3, 4, 5]
    print(np.var(a))


def make_dic():
    dic = {}
    a = [463, 458, 468, 481, 392, 400, 299, 298, 297, 295]
    for i in range(10):
        dic[a[i]] = i
    print(dic)


def check_dic():
    dic = {463: 0, 458: 1, 468: 2, 481: 3, 392: 4, 400: 5, 299: 6, 298: 7, 297: 8, 295: 9}
    a = [463, 4000]
    for i in range(2):
        if i < a[i]:
            # i = 'b'
            print('一个')
        # print(i)
        # if i in dic:
        #     print(i, dic[i])


def esay_print():
    a = 1
    b = a

    for i in range(10):
        b = i
        print(b)
        # if i == 5:
        #     pass
        # else:
        #     print(i)

        # print(i)


if __name__ == '__main__':
    # t()
    # cul_time()
    # change_time()
    # tes_00()
    # make_all_od_2()
    # cuaclu()
    # make_var()
    # make_dic()
    # check_dic()
    esay_print()




















