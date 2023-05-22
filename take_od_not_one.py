import time


def make_od_6_10():
    path = '/data/WorkMind/data/student/d/one_hour/10_list.txt'
    save_path = '/data/WorkMind/data/student/d/one_hour/10_od.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    num = 0
    wrong_car = []  # 这辆车已经找不到数据对了, 遇到这辆车需要跳过
    car_dic = {}  # 数据类型 int
    for i, k in enumerate(f):
        key = i
        print(i, car_dic, wrong_car)
        car = k.split(',')  # 此时的car 里面的所有数据都是str格式
        if int(car[0]) in wrong_car:  # 如果在wrong_car 列表里面 就跳过继续
            continue
        if i + 3 > len(f):  # 最后3条数据 一个完成的od，一定需要3条数据以上
            break
        if int(car[0]) in car_dic and key <= car_dic[int(car[0])]:
            print('有一个')
            continue
        if car[3] == '0':  # 此时空车  状态是0
            for ii, j in enumerate(f[key + 1:]):  # 同一辆车的第二个点开始找
                car2 = j.split(',')
                if car[0] == car2[0] and car2[3] != car[3]:
                    # 此时上车    状态是-1 载客了，这个时候比较重要,如果下面的不符合直接break   一旦开始载客，就要一直找到下车的时候
                    for iii, h in enumerate(f[key + ii + 2:]):
                        car3 = h.split(',')
                        if int(key + ii + 2 + iii) >= len(f):
                            wrong_car.append(int(car[0]))  # 已经找到最后一条了还没有找到，此时这辆车就不需要再找了包括下次循环
                            break
                        if car[0] == car3[0] and car3[3] != car2[3] and int(car3[6]) - int(
                                car2[6]) > 300:  # 此时下车了，状态是空车，下面无论怎么执行都要break
                            # if int(car3[6]) - int(car2[6]) > 300:
                            car_dic[int(car[0])] = int(key + ii + 2 + iii)
                            timeArray_1 = time.localtime(int(car2[6]))  # 上车的时间
                            otherStyleTime_1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_1)
                            timeArray_2 = time.localtime(int(car3[6]))  # 下车的时间
                            otherStyleTime_2 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray_2)

                            od = ''
                            od += car2[0]
                            od += ','
                            od += otherStyleTime_1
                            # od += car2[6].replace('\n', '')
                            od += ','
                            od += car2[1]
                            od += ','
                            od += car2[2]
                            od += ','
                            od += otherStyleTime_2
                            # od += car3[6].replace('\n', '')
                            od += ','
                            od += car3[1]
                            od += ','
                            od += car3[2]
                            print(od, num)
                            ff.write(f'{od}\n')
                            num += 1
                            break  # 检测到下车
                    break  # 检测到上车
    print('统计完成，总共：', num)


if __name__ == '__main__':
    make_od_6_10()
