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
    path1 = '/data/WorkMind/data/jiaxing/cascade_518/FASTV4/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/ImageSets/Main/train.txt'
    path2 = '/data/WorkMind/data/jiaxing/cascade_518/FASTV4/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/ImageSets/Main/val.txt'
    path3 = '/data/WorkMind/data/jiaxing/cascade_518/FASTV4/faster-rcnn.pytorch/data/VOCdevkit2007/VOC2007/ImageSets/Main/trainval.txt'
    # 29092
    f1 = open(path1, 'w')
    f2 = open(path2, 'w')
    f3 = open(path3, 'w')
    num1 = 50000
    num2 = 50000
    num3 = 50000
    for i in range(50000, 79092):
        if 50000<= num1 < 700000:
            f2.write(str(num1).zfill(6) + '\n')

        if 70000 < num2:
            f1.write(str(num2).zfill(6) + '\n')


        if num3 < 79093:
            f3.write(str(num3).zfill(6) + '\n')
            num1 += 1
            num2 += 1
            num3 += 1


if __name__ == '__main__':
    # take_txt()
    make_main()
