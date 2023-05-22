import os
import csv
from geopy.distance import geodesic as GD


def points():
    file = open('../data/od.txt', 'r')  # 打开文件
    lines = file.readlines()  # 对文件进行逐行读取
    edge = len(lines)  # 网络边的条数
    # edge = 0  # 网络边的条数
    net = dict()  # 创建空字典，value为元组形
    for line in lines:  # 遍历每行数据
        whole = line.split()  # 以空格为分隔符，包含 \n
        k = whole[0]  # 取出每行数据的第一个数
        if k != whole[1]:
            tup1 = (whole[1],)  # 取出每行数据的第二个数，存入元组
            # edge += 1
            if k not in net:  # 如果字典中不存在与k相同的key，就添加key-value值
                net[k] = tup1
            else:  # 如果字典中存在与k相同的key值，就将对于的值添加到value中
                net[k] = net[k] + tup1
    file.close()
    # calculate_du(edge, net)
    # file1 = open("节点的度.csv", 'w', encoding='utf-8', newline='')  # 创建节点的度.csv文件
    # csv_writer = csv.writer(file1)  # 构建csv写入对象
    # csv_writer.writerow(["节点", "度"])  # 构建列表头
    count = 0  # 计算节点的个数
    for key in net:
        count += 1
        # f = key
        # d = len(net[key])
    #     csv_writer.writerow([f, d])
    # file1.close()
    # 网络平均度
    print("网络平均度为：{}".format(2 * edge / count))


def calculate_du(edge, net):
    # 节点的度
    file1 = open("节点的度.csv", 'w', encoding='utf-8', newline='')  # 创建节点的度.csv文件
    csv_writer = csv.writer(file1)  # 构建csv写入对象
    csv_writer.writerow(["节点", "度"])  # 构建列表头
    count = 0  # 计算节点的个数
    for key in net:
        count += 1
        f = key
        d = len(net[key])
        csv_writer.writerow([f, d])
    file1.close()
    # 网络平均度
    print("网络平均度为：{}".format(2 * edge / count))


def make_txt():
    path1 = '../data/od1.txt'
    path2 = '../data/od2.txt'
    f = open(path1, 'r').readlines()
    ff = open(path2, 'r').readlines()
    f_write = open('../data/od.txt', 'w')
    for i, k in enumerate(f):
        f_write.write(k.replace('\n', '') + ' ' + ff[i])

    print(len(f),len(ff))


def make_not_repeat():
    path = '../data/od.txt'
    path_w = '../data/od_not_repeat.txt'
    f = open(path, 'r').readlines()
    f_write = open(path_w, 'w')
    for i in f:
        ii = i.replace('\n', '')
        li = ii.split(' ')
        if li[0] != li[1]:
            f_write.write(i)

def make_txt_du():
    du = []
    use_du = {}
    path1 = '../data/od1.txt'
    path2 = '../data/od2.txt'
    path3 = '../data/lone1.txt'
    f = open(path1, 'r').readlines()
    ff = open(path2, 'r').readlines()
    fff = open(path3, 'r').readlines()
    f_write = open('../data/use_du.txt', 'w')
    for i, k in enumerate(f):
        if k not in du:
            du.append(k)
            dimention = fff[i]
            di = dimention.split('\t')
            f_write.write(k.replace('\n', '') + ' ' + di[0] + ' ' + di[1] + '\n')

    for ii, kk in enumerate(ff):
        if kk not in du:
            du.append(k)
            dimention = fff[ii]
            di = dimention.split('\t')
            f_write.write(kk.replace('\n', '') + ' ' + di[2] + ' ' + di[3])

    f_write.close()

    print(len(f),len(ff))

def caclu_leng(dimension):
    # pair数据格式，(latitude, longitude), 纬度和经度， 注意纬度和经度的取值范围
    Abuja = (dimension[1],dimension[0])
    Dakar = (dimension[3],dimension[2])
    # Dakar = (39.98919,116.30994)
    lone = round(GD(Abuja, Dakar).km, 3)
    return lone


def long():
    path = '../data/lone.txt'
    f = open(path, 'r').readlines()
    all = []
    for i in f:
        dimension = i.replace('\n', '').split('\t')
        if len(dimension) == 4:
            li = caclu_leng(dimension)
            if li != 0.0:
                all.append(li)

    print('平均长度为：', sum(all)/len(all))


def average_lone():
    path = '../data/use_du.txt'
    f = open(path, 'r').readlines()
    all_lone = []
    for i, k in enumerate(f[:-1]):
        dimension = k.replace('\n', '').split(' ')
        for j in f[i+1:]:
            dimension2 = j.replace('\n', '').split(' ')
            Abuja = (dimension[2], dimension[1])
            Dakar = (dimension2[2], dimension2[1])
            # Dakar = (39.98919,116.30994)
            lone = round(GD(Abuja, Dakar).km, 3)
            all_lone.append(lone)

    print('平均长度:', sum(all_lone)/len(all_lone))


def aggregation_factor():
    path = '../data/od_not_repeat.txt'
    f = open(path, 'r').readlines()
    li = []
    count = []
    for i, k in enumerate(f[:-1]):
        point1 = k.split(' ')[0]
        num = 1
        take_li = []
        take_li.append(k.split(' ')[0])
        for j in f[i+1:]:
            if i in j.split(' '):
                num += 1
                if j.split(' ')[0]




if __name__ == '__main__':
    # points()
    # make_txt()
    # make_not_repeat()
    # make_txt_du()
    # caclu_leng()
    # long()
    # average_lone()
    aggregation_factor()



















