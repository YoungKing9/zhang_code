# 代码1 txt格式转xml
from xml.dom.minidom import Document
import os
import cv2
import random
import re
import shutil




# def makexml(txtPath, xmlPath, picPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
# def makexml(picPath, txtPath, xmlPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
def makexml(picPath, xmlPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
    """此函数用于将yolo格式txt标注文件转换为voc格式xml标注文件
    """
    # dic = {'0': "body",  # 创建字典用来对类型进行转换
    #
    #        }
    dic = {0: 'shoes', 1: 'bin', 2: 'pedestal', 3: 'wire', 4: 'socket', 5: 'cat', 6: 'dog', 7: 'desk_rect',
           8: 'desk_circle', 9: 'weighing-scale'}
    # walk_train_list(picPath)
    files = open(picPath, 'r').readlines()
    # files = os.listdir(txtPath)
    # files = files[93941:]
    print(len(files))
    # num_pic = 140819     93941报错，删除一张
    # num_pic = 93942
    num_pic = 1
    f_write = open('/data/WorkMind/data/student/zhang_code/data/wrong_pic.txt', 'w')

    for i, name in enumerate(files[:90000]):
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)
        # txtFile = open(txtPath + name)
        # 把图片复制到 voc下面
        pic_name = num_pic
        pic = name.split('JPEGImages')
        cut_num = -4

        if (pic[0] + 'labels' + pic[1].replace('\n', '')).split('.')[-1] == 'png':
            print(num_pic)
        num_pic += 1

# f"{str(num_pic).zfill(6)}" + ".jpg")

# /data/VOC/ABBY/darknet/version2.1.18/train.txt
# /data/VOC/ABBY/darknet/version2.1.18/val.txt

if __name__ == "__main__":
    picPath = "/data/VOC/ABBY/darknet/version2.1.18/train.txt"  # 图片所在文件夹路径，后面的/一定要带上  140818
    # txtPath = "/root/autodl-tmp/CrowdHuamn/labels/train/"  # txt所在文件夹路径，后面的/一定要带上
    xmlPath = "/data/VOC/voc2017_rcnn/VOC2007/Annotations/"  # xml文件保存路径，后面的/一定要带上
    # xmlPath = "/data/VOC/voc2017/test/"  # xml文件保存路径，后面的/一定要带上
    makexml(picPath, xmlPath)
