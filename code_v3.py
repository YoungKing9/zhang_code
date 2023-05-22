import os
import time



def make_all_od_2():
    path = '/data/WorkMind/data/student/d/7_8.txt'
    save_path = '/data/WorkMind/data/student/d/all_od_3.txt'

    f = open(path, 'r').readlines()
    ff = open(save_path, 'w')
    num = 0
    for i, k in enumerate(f):
        # if num < 10:
        car = k.split(',')
        if car[3] == '0':  # 此时空车
            for ii, j in enumerate(f[i + 1:]):
                car2 = j.split(',')
                if car[0] == car2[0] and car2[3] != car[3] and (int(car2[6]) - int(car[6])) < 300:  # 此时上车
                    for iii, h in enumerate(f[i + ii + 2:]):
                        car3 = h.split(',')
                        if car[0] == car3[0] and car3[3] == car2[3]:  # 此时下车
                            for iiii, g in enumerate(f[i + ii + iii + 3:]):
                                car4 = g.split(',')
                                if car[0] == car4[0] and car4[3] != car3[3] and (int(car3[6]) - int(car[6])) > 300 and (int(car4[6]) - int(car3[6])) < 300:
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


if __name__ == '__main__':
    make_all_od_2()






