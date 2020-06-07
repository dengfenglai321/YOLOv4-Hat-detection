import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import bs4
from PIL import Image


classes = ["person", "hat"]  #为了获得cls id

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    global none_counts

    # 输入文件xml
    in_file = open('./labels/valid/%s.xml' % (image_id))
    # 输出label txt
    out_file = open('./labels/txt_valid/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    print(image_id)

    if size == None:
        print('{}不存在size字段'.format(image_id))
        # 第一个处理方法
        img = Image.open('./VOCPerson/JPEGImages/' + image_id + '.jpg')
        w, h = img.size  # 大小/尺寸
        print('{}.xml缺失size字段, 读取{}图片得到对应 w：{} h：{}'.format(image_id, image_id, w, h))
        # # 第二种处理方法
        # # 移除xml
        # os.remove('./VOCPerson/Annotations/' + image_id + '.xml')
        # # 移除上面被移除掉xml对应的jpg
        # os.remove('./VOCPerson/JPEGImages/' + image_id + '.jpg')

        none_counts += 1
    else:

        w = int(size.find('width').text)
        h = int(size.find('height').text)
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')



if __name__=='__main__':
    xml_count = 0
    none_counts = 0
    list_file = os.listdir('./labels/valid/')
    for file in list_file:
        print(file)
        # image_id = file.replace('.xml', '')
        image_id = file.split('.')[0]
        convert_annotation(image_id)
        xml_count = xml_count + 1
    print('没有size字段的xml文件数目：{}'.format(none_counts))
    print('总xml个数是 {}'.format(xml_count))



