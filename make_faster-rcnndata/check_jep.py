# 1check if there are corrputed images in JPEG
# 2check if there are '0' cordinate in xml file
# 3chechk if xmin coordinates have 0 value,todo:checkif max is greater than width

# 111111111111111111111111
import numpy as np
from PIL import Image
import xml.dom.minidom
import os

if __name__ == '__main__':
    badFilesList = []
    curDir = '/data/VOC/voc2017/VOC2007/VOC2007/JPEGImages'
    for root, dirs, files in os.walk(curDir):  # print(files)
        # check the corrupted file in curDir
        for each in files:
            if each.endswith('.jpg') or each.endswith('.JPG') or each.endswith('.jpeg') or each.endswith(
                    '.JPEG'):  # print(each)
                try:
                    im = Image.open(os.path.join(root, each))  # im.show()
                    # print(each+"is ok")
                    im = np.array(im, dtype=np.float32)  # added recently at Feb.23
                except Exception as e:
                    print('corrupted file:', os.path.join(root, each))
                    badFilesList.append(os.path.join(root, each))  # del the corrupted files
                if len(badFilesList) != 0:
                    for each in badFilesList:
                        try:
                            # os.remove(each)
                            print("pretend to remove" + each)
                        except Exception as e:
                            print('Del file: %s failed, %s' % (each, e))
                            pass
        if len(badFilesList) == 0:
            print("no corrupted filesï¼already checked ", len(files))
        else:
            print("corrputed files are above----------------------------", "already checked ", len(files))
    # 222=222222222222222222222222
    # pause_=input()
    path = r"/data/VOC/voc2017/VOC2007/Annotations/"
    Assertion_provoker_y = []
    Assertion_provoker_x = []
    files = os.listdir(path)
    for file in files:
        file = os.path.join(path, file)
        dom = xml.dom.minidom.parse(file)
        root = dom.documentElement
        size = dom.getElementsByTagName("size")

        height = dom.getElementsByTagName("height")[0]
        width = dom.getElementsByTagName("width")[0]
        width = width.childNodes[0].data
        height = height.childNodes[0].data

        objects = dom.getElementsByTagName("object")
        for object in objects:
            bndbox = object.getElementsByTagName('bndbox')[0]  ########
            xmin = bndbox.getElementsByTagName('xmin')[0]
            xmin_data = xmin.childNodes[0].data
            ymin = bndbox.getElementsByTagName('ymin')[0]
            ymin_data = ymin.childNodes[0].data
            xmax = bndbox.getElementsByTagName('xmax')[0]
            xmax_data = xmax.childNodes[0].data
            ymax = bndbox.getElementsByTagName('ymax')[0]
            ymax_data = ymax.childNodes[0].data
            # check if the xmin or yin is 0
            if (int(xmin_data) == 0):
                print(file, "the x of it is 0")
            if (int(ymin_data) == 0):
                print(file, "the y of it is 0")
            ##check if min is greater than max
            if (int(ymin_data) > int(ymax_data)):
                Assertion_provoker_y.append(file)
            if (int(xmin_data) > int(xmax_data)):
                Assertion_provoker_x.append(file)
            # check if x is greater than width,or y is greater than height
            if (int(xmax_data) > int(width)):
                Assertion_provoker_x.append(file)
            if (int(xmin_data) > int(width)):
                Assertion_provoker_x.append(file)
            if (int(ymax_data) > int(height)):
                Assertion_provoker_y.append(file)
            if (int(ymin_data) > int(height)):
                Assertion_provoker_y.append(file)
    print("checking assertion error done,already checked", len(files),
          "files,with {} y_provoker".format(len(Assertion_provoker_y)))
    print("checking assertion error done,already checked", len(files),
          "files,with {} x_provoker".format(len(Assertion_provoker_x)))
    # print(Assertion_provoker_x)
#######################################################