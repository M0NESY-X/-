import os,sys

# 按行合并 两个txt文件
# 打开所需要合并的两个txt文件
file1path = 'gpsindex01.txt'
file2path = 'dataLabel.txt'

file_1 = open(file1path, 'r', encoding='utf-8')
file_2 = open(file2path, 'r', encoding='utf-8')

list1 = []
for line in file_1.readlines():
    ss = line.strip()
    list1.append(ss)
file_1.close()

list2 = []
for line in file_2.readlines():
    ss = line.strip()
    list2.append(ss)
file_2.close()

# 创建新的txt文件，用来保存，'annotation/result2.txt'为保存路径
file_new = open('gpsindex+label01.txt', 'w', encoding='utf-8')
for i in range(len(list1)):
    # 将两个txt文件合并到一行 中间用分隔符隔开
    sline = list1[i] + '\t' + list2[i]
    # 写入新的txt文件 换行
    file_new.write(sline+'\n')
file_new.close()