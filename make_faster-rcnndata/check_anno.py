import os
import xml.etree.ElementTree as ET


def read_xml():
    xmlpath = '/data/WorkMind/data/student/zhang_code/make_faster-rcnndata/data/000002.xml'
    dom = ET.parse(xmlpath)
    root = dom.getroot()
    # print(root.find('filename').text)
    print(root.find('filename').text)



def read_xml_v2():
    pass


def change_xml():
    pass



def yolov5_xml():
    pass



if __name__ == '__main__':
    read_xml()  # 读取xml
    # read_xml_v2() # 读取xml，方式2
    # change_xml() # 修改xml并保存
    # yolov5_xml() # 生成小批量训练数据


















