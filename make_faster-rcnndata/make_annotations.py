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

    for i, name in enumerate(files[:100000]):
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)
        # txtFile = open(txtPath + name)
        # 把图片复制到 voc下面
        pic_name = num_pic
        shutil.copy(name.replace('\n', ''), f"/data/VOC/voc2017_rcnn/VOC2007/JPEGImages/{str(num_pic).zfill(6)}.jpg")
        pic = name.split('JPEGImages')
        cut_num = -4
        txtList = []
        if (pic[0] + 'labels' + pic[1].replace('\n', '')).split('.')[-1] == 'jpg':
            txtFile = open((pic[0] + 'labels' + pic[1].replace('\n', '')).replace('jpg', 'txt'))
            txtList = txtFile.readlines()
        elif (pic[0] + 'labels' + pic[1].replace('\n', '')).split('.')[-1] == 'png':
            txtFile = open((pic[0] + 'labels' + pic[1].replace('\n', '')).replace('png', 'txt'))
            txtList = txtFile.readlines()
        elif (pic[0] + 'labels' + pic[1].replace('\n', '')).split('.')[-1] == 'JPEG':
            txtFile = open((pic[0] + 'labels' + pic[1].replace('\n', '')).replace('JPEG', 'txt'))
            txtList = txtFile.readlines()
            cut_num = -5

        name = name.replace('\n', '')
        img = cv2.imread(name)
        # print(txtList)
        Pheight, Pwidth, Pdepth = img.shape



        folder = xmlBuilder.createElement("folder")  # folder标签
        foldercontent = xmlBuilder.createTextNode("VOC2007")
        folder.appendChild(foldercontent)
        annotation.appendChild(folder)  # folder标签结束

        filename = xmlBuilder.createElement("filename")  # filename标签

        # filenamecontent = xmlBuilder.createTextNode(name[0:cut_num] + ".jpg")
        filenamecontent = xmlBuilder.createTextNode(f"{str(num_pic).zfill(6)}" + ".jpg")

        filename.appendChild(filenamecontent)
        annotation.appendChild(filename)  # filename标签结束

        size = xmlBuilder.createElement("size")  # size标签
        width = xmlBuilder.createElement("width")  # size子标签width
        widthcontent = xmlBuilder.createTextNode(str(Pwidth))
        width.appendChild(widthcontent)
        size.appendChild(width)  # size子标签width结束

        height = xmlBuilder.createElement("height")  # size子标签height
        heightcontent = xmlBuilder.createTextNode(str(Pheight))
        height.appendChild(heightcontent)
        size.appendChild(height)  # size子标签height结束

        depth = xmlBuilder.createElement("depth")  # size子标签depth
        depthcontent = xmlBuilder.createTextNode(str(Pdepth))
        depth.appendChild(depthcontent)
        size.appendChild(depth)  # size子标签depth结束

        annotation.appendChild(size)  # size标签结束

        for j in txtList:
            # print('j', j)
            oneline = j.strip().split(" ")
            object = xmlBuilder.createElement("object")  # object 标签
            picname = xmlBuilder.createElement("name")  # name标签
            namecontent = xmlBuilder.createTextNode(dic[int(oneline[0])])
            picname.appendChild(namecontent)
            object.appendChild(picname)  # name标签结束

            pose = xmlBuilder.createElement("pose")  # pose标签
            posecontent = xmlBuilder.createTextNode("Unspecified")
            pose.appendChild(posecontent)
            object.appendChild(pose)  # pose标签结束

            truncated = xmlBuilder.createElement("truncated")  # truncated标签
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)  # truncated标签结束

            difficult = xmlBuilder.createElement("difficult")  # difficult标签
            difficultcontent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultcontent)
            object.appendChild(difficult)  # difficult标签结束

            bndbox = xmlBuilder.createElement("bndbox")  # bndbox标签
            xmin = xmlBuilder.createElement("xmin")  # xmin标签
            mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            xminContent = xmlBuilder.createTextNode(str(mathData))
            xmin.appendChild(xminContent)
            bndbox.appendChild(xmin)  # xmin标签结束

            ymin = xmlBuilder.createElement("ymin")  # ymin标签
            mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            yminContent = xmlBuilder.createTextNode(str(mathData))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)  # ymin标签结束

            xmax = xmlBuilder.createElement("xmax")  # xmax标签
            mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            xmaxContent = xmlBuilder.createTextNode(str(mathData))
            xmax.appendChild(xmaxContent)
            bndbox.appendChild(xmax)  # xmax标签结束

            ymax = xmlBuilder.createElement("ymax")  # ymax标签
            mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            ymaxContent = xmlBuilder.createTextNode(str(mathData))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)  # ymax标签结束

            object.appendChild(bndbox)  # bndbox标签结束

            annotation.appendChild(object)  # object标签结束

        f = open(xmlPath + f"{str(num_pic).zfill(6)}.xml", 'w')
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        num_pic += 1
        f.close()
    print('图片一共有:', num_pic)


# /data/VOC/ABBY/darknet/version2.1.18/train.txt
# /data/VOC/ABBY/darknet/version2.1.18/val.txt

if __name__ == "__main__":
    picPath = "/data/VOC/ABBY/darknet/version2.1.18/train.txt"  # 图片所在文件夹路径，后面的/一定要带上  140818
    # txtPath = "/root/autodl-tmp/CrowdHuamn/labels/train/"  # txt所在文件夹路径，后面的/一定要带上
    xmlPath = "/data/VOC/voc2017_rcnn/VOC2007/Annotations/"  # xml文件保存路径，后面的/一定要带上
    # xmlPath = "/data/VOC/voc2017/test/"  # xml文件保存路径，后面的/一定要带上
    makexml(picPath, xmlPath)
