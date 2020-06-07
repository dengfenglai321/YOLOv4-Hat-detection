import os
import glob
import json
import shutil
import numpy as np
import xml.etree.ElementTree as ET

img_train = './images/train/'
img_val = './images/valid/'

label_train = './labels/train/'
label_val = './labels/valid/'

allimgs = glob.glob('原始数据集/train/' + "/*.jpg")
allimgs = np.sort(allimgs)
np.random.seed(100)
np.random.shuffle(allimgs)

train_ratio = 0.9
train_num = int(len(allimgs) * train_ratio)

# 得到训练和验证数据集列表
img_list_train = allimgs[:train_num]
img_list_val = allimgs[train_num:]

# 创建文件夹
if os.path.exists(img_train):
    shutil.rmtree(img_train)
    os.mkdir(img_train)
else:
    os.mkdir(img_train)

if os.path.exists(img_val):
    shutil.rmtree(img_val)
    os.mkdir(img_val)
else:
    os.mkdir(img_val)

if os.path.exists(label_train):
    shutil.rmtree(label_train)
    os.mkdir(label_train)
else:
    os.mkdir(label_train)

if os.path.exists(label_val):
    shutil.rmtree(label_val)
    os.mkdir(label_val)
else:
    os.mkdir(label_val)

# 移动val数据到指定位置
for i in img_list_val:
    img_id = i.split('.')[0].split('/')[2]
    print(img_id)
    # jpg
    shutil.copy(i, img_val + img_id + '.jpg')
    # xml
    shutil.copy('原始数据集/label/' + 'new_' + img_id + '.xml', label_val + img_id + '.xml')

# 移动train数据到指定位置
for i in img_list_train:
    img_id = i.split('.')[0].split('/')[2]
    print(img_id)
    # jpg
    shutil.copy(i, img_train + img_id + '.jpg')
    # xml
    shutil.copy('原始数据集/label/' + 'new_' + img_id + '.xml', label_train + img_id + '.xml')

