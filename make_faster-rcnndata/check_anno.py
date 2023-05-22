
from xml.etree.ElementTree import ElementTree ,Element
import  xml.dom.minidom
import os
import xml.etree.ElementTree as ET
from xml.etree import cElementTree as ET
import pandas as pd
from xml.etree.ElementTree import Element

path ="/data/VOC/voc2017v2/Annotations/"
Assertion_provoker_x = []
Assertion_provoker_y = []
sucess_file = []
files = os.listdir(path)
# for file in files:
#     file =os.path.join(path ,file)
#     dom = xml.dom.minidom.parse(file)
#     # 获得根节点
#     print(file)
#
#     root = dom.documentElement
#     objects =root.getAttribute("size")
#     # bndbox = objects.getElementsByTagName()
#     # bndbox = object.getElementsByTagName('bndbox')[0]
#     bndbox = objects
#     xmin = bndbox.getElementsByTagName('xmin')[0]
#     xmin_data =xmin.childNodes[0].data
#     xmax = bndbox.getElementsByTagName('xmax')[0]
#     xmax_data =xmin.childNodes[0].data
#
#     ymin = bndbox.getElementsByTagName('ymin')[0]
#     ymin_data =xmax.childNodes[0].data
#     ymax = bndbox.getElementsByTagName('ymax')[0]
#     ymax_data =xmax.childNodes[0].data
#     print(xmax_data, ymax_data)


for i in files:
    # tree = ET.parse("1.xml")
    file =os.path.join(path , i)

    root = ET.fromstring(file)
    # 读取xml文件
    # tree = ET.ElementTree(file="text.xml")
    # root = tree.getroot()
    data = list()
    for child in root:
        data1 = list()
        for son in child:
            data1.append(son.text)
        data.append(data1)

    df = pd.DataFrame(data, columns=['shape', 'degrees', 'sides'])
    print(df)


    # for child in root:
    #     print("tag:", child.tag)
    #     print("tag:", child.text)
    #     print("attrib:", child.attrib)

