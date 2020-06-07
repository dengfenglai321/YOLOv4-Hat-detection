# 根据训练数据集和验证数据集persontrain.txt and personvalid.txt
import os, random, shutil

trainDir = 'images/train/'
validDir = 'images/valid/'

train_pathDir = os.listdir(trainDir)  # 取图片的原始路径
print('训练集图片数目: {}'.format(len(train_pathDir)))

valid_pathDir = os.listdir(validDir)  # 取图片的原始路径
print('验证集图片数目: {}'.format(len(valid_pathDir)))

# 删除persontrain.txt and personvalid.txt
if(os.path.exists('train.txt')):
     os.remove('train.txt')
     print('删除train.txt成功')

if(os.path.exists('valid.txt')):
     os.remove('valid.txt')
     print('删除valid.txt成功')

def text_save(root, filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = 'data/' + root + s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

if __name__ == '__main__':
    text_save(trainDir, './train.txt', train_pathDir)
    text_save(validDir, './valid.txt', valid_pathDir)
    print('train.txt 有 {} 行'.format(len([i for i in open('./train.txt', 'r')])))
    print('valid.txt 有 {} 行'.format(len([i for i in open('./valid.txt', 'r')])))

