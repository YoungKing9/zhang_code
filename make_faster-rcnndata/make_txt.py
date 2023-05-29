# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random

trainval_percent = 0.8  # trainval占比例多少
train_percent = 0.7  # test数据集占比例多少
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\Main'
total_xml = os.listdir(xmlfilepath)
#
# num = len(total_xml)
num = 50000
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
# list = 50000
# tv = int
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('/data/VOC/voc2017_rcnn/VOC2007/ImageSets/Main/trainval.txt', 'w')
ftest =     open('/data/VOC/voc2017_rcnn/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain =    open('/data/VOC/voc2017_rcnn/VOC2007/ImageSets/Main/train.txt', 'w')
fval =      open('/data/VOC/voc2017_rcnn/VOC2007/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()