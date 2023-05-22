# 代码1 txt格式转xml
from xml.dom.minidom import Document
import os
import cv2
import random
import re
import shutil


def walk_train_list(path, suffix: list):
    file_list = []
    suffix = [s.lower() for s in suffix]
    if not os.path.exists(path):
        print("not exist path {}".format(path))
        return []

    if os.path.isfile(path):
        return [path, ]

    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1].lower()[1:] in suffix:
                file_list.append(os.path.join(root, file))

    try:
        file_list.sort(key=lambda x: int(re.findall('\d+', os.path.splitext(os.path.basename(x))[0])[0]))
    except:
        pass
    random.shuffle(file_list)
    return file_list


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
    print(len(files))
    num_pic = 1

    for i, name in enumerate(files):
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)
        # txtFile = open(txtPath + name)
        # 把图片复制到 voc下面
        pic_name = num_pic
        # shutil.copy(name.replace('\n', ''), f"/data/VOC/voc2017v2/JPEGImages/{str(num_pic).zfill(6)}.jpg")
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
        # print(name)
        # save_path = name.split('JPEGImages')[-1]
        # # print(xmlPath, save_path)
        # save_paths = xmlPath + save_path.replace(save_path.split('/')[-1], '')
        # # print(save_paths)
        # if not os.path.exists(save_paths):
        #     os.makedirs(save_paths)

        # f = open(save_paths + f"{str(num_pic).zfill(6)}.xml", 'w')
        f = open(xmlPath + f"{str(num_pic).zfill(6)}.xml", 'w')
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        num_pic += 1

        f.close()


# /data/VOC/ABBY/darknet/version2.1.18/train.txt
# /data/VOC/ABBY/darknet/version2.1.18/val.txt

if __name__ == "__main__":
    picPath = "/data/VOC/ABBY/darknet/version2.1.18/train_faster.txt"  # 图片所在文件夹路径，后面的/一定要带上
    # txtPath = "/root/autodl-tmp/CrowdHuamn/labels/train/"  # txt所在文件夹路径，后面的/一定要带上
    xmlPath = "/data/VOC/voc2017v2/Annotations/"  # xml文件保存路径，后面的/一定要带上
    # xmlPath = "/data/VOC/voc2017/test/"  # xml文件保存路径，后面的/一定要带上
    makexml(picPath, xmlPath)
