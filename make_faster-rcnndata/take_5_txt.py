# xml文件保存路径，后面的/一定要带上
import os
import time


def take_txt():
    picPath = "/data/VOC/ABBY/darknet/version2.1.18/train.txt"  # 图片所在文件夹路径，后面的/一定要带上
    # txtPath = "/root/autodl-tmp/CrowdHuamn/labels/train/"  # txt所在文件夹路径，后面的/一定要带上
    xmlPath = "/data/VOC/voc2017/Annotations/"
    picPath2 = "/data/VOC/ABBY/darknet/version2.1.18/train_faster.txt"
    f = open(picPath, 'r').readlines()
    ff = open(picPath2, 'w')
    num = 0
    for i in f:
        if num < 50000:
            ff.write(i)
            num += 1

def make_main():
    path1 = '/data/VOC/voctest/VOC2007/ImageSets/Main/train.txt'
    path2 = '/data/VOC/voctest/VOC2007/ImageSets/Main/val.txt'
    path3 = '/data/VOC/voctest/VOC2007/ImageSets/Main/trainval.txt'
    # 29092
    f1 = open(path1, 'w')
    f2 = open(path2, 'w')
    f3 = open(path3, 'w')
    num1 = 1
    num2 = 1
    num3 = 1
    for i in range(50000, 79092):
        if 2000 < num1 <= 3000:    # 测试集合
            f2.write(str(num1).zfill(6) + '\n')

        if 1 <= num2 <= 2000:     # 训练集合
            f1.write(str(num2).zfill(6) + '\n')


        if num3 <= 3000:   # 总的
            f3.write(str(num3).zfill(6) + '\n')
            num1 += 1
            num2 += 1
            num3 += 1


if __name__ == '__main__':
    # take_txt()
    make_main()
