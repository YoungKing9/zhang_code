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
    # count = 0  # 计算节点的个数
    # for key in net:
    #     count += 1
        # f = key
        # d = len(net[key])
    #     csv_writer.writerow([f, d])
    # file1.close()
    # 网络平均度
    print("网络平均度为：{}".format(2 * edge / len(net)))


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

    print(len(f), len(ff))


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
            du.append(kk)
            dimention = fff[ii]
            di = dimention.split('\t')
            f_write.write(kk.replace('\n', '') + ' ' + di[2] + ' ' + di[3])

    f_write.close()

    print(len(f), len(ff))


def caclu_leng(dimension):
    # pair数据格式，(latitude, longitude), 纬度和经度， 注意纬度和经度的取值范围
    Abuja = (dimension[1], dimension[0])
    Dakar = (dimension[3], dimension[2])
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

    print('平均长度为：', sum(all) / len(all))


def average_lone():   # 计算任意两个点的距离并且求平均值
    path = '../data/use_du.txt'
    f = open(path, 'r').readlines()
    all_lone = []
    for i, k in enumerate(f[:-1]):
        dimension = k.replace('\n', '').split(' ')
        for j in f[i + 1:]:
            dimension2 = j.replace('\n', '').split(' ')
            Abuja = (dimension[2], dimension[1])    # 这个是经纬度
            Dakar = (dimension2[2], dimension2[1])  # 另一个点的经纬度
            # Dakar = (39.98919,116.30994)
            lone = round(GD(Abuja, Dakar).km, 3)     #立功GD库计算两个点的距离
            all_lone.append(lone)

    print('平均长度:', sum(all_lone) / len(all_lone))


def aggregation_factor():    # 计算聚集系数
    path = '../data/od_not_repeat.txt'
    f = open(path, 'r').readlines()
    all_id = []
    count = []
    for i, k in enumerate(f):  # 这个循环把所有的节点添加到all_id列表里面
        ii = k.replace('\n', '').split(' ')
        for j in ii:
            if j not in all_id:
                all_id.append(j)

    for id in all_id:   # 计算单个节点的聚集系数
        num1 = 0        # 单个节点构成的边的数量
        id_list = []
        for l in f:     # l 为  213 123
            l_split = l.replace('\n', '').split(' ')
            if id in l_split:    # 如果节点在一个节点对里面， num1 就加 1
                num1 += 1
                for l_s in l_split:
                    if l_s not in id_list:
                        id_list.append(l_s)    # 将所有包含要计算的节点的节点对，元素添加到id_list
        id_list.remove(id)      # 最后列表面除掉要计算的节点
        num2 = 0
        for m in f:
            m_split = m.replace('\n', '').split(' ')
            if m_split[0] in id_list and m_split[1] in id_list:  # 如果两个节点都在id_list, 就说明这两个点都和要计算的节点id连接，并且它俩也能连接
                num2 += 1
        if num1 != 0 and num2 != 0:
            juji_index = num2 / num1   # 最后求单个节点的聚集系数
            count.append(juji_index)

    print('聚集系数为：', sum(count) / len(count))



def in_out():    #计算流量比
    path = '../data/od_not_repeat.txt'
    f = open(path, 'r').readlines()
    all_id = []   # 不重复，所有的节点
    count = []    # 计算每个节点的流量比
    for i, k in enumerate(f):    # 这个循环把所有的节点添加到all_id列表里面
        ii = k.replace('\n', '').split(' ')
        for j in ii:
            if j not in all_id:
                all_id.append(j)

    for id in all_id:
        num1 = 0  # 单个节点流入 的数量
        num2 = 0  # 单个节点流出 的数量
        for l in f:
            l_split = l.replace('\n', '').split(' ')
            if l_split[1] == id:
                num1 += 1
            if l_split[0] == id:
                num2 += 1
        if num1 != 0 and num2 != 0:
            id_index = num1 - num2 / num1 + num2
            count.append(id_index)

    print('流量比为：', sum(count) / len(count))


if __name__ == '__main__':
    # points()   # 计算评论度
    # make_txt()
    # make_not_repeat()
    # make_txt_du()
    # caclu_leng()
    # long()
    average_lone()    # 计算平均长度
    # aggregation_factor()  # 计算聚集系数
    # in_out()  # 计算流量系数
