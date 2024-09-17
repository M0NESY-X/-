import os
def str_substitute(folder_path,old_str,new_str):
    file_list = os.listdir(folder_path)
    for file in file_list:
        file_path = os.path.join(folder_path,file)
        with open(file_path, "r") as f:  # 以只读方式打开文件
                data = f.read()  # 读取文件，读取为一个字符串
                str_replace = data.replace(old_str,new_str)#将字符串中的某个字符进行替换
                with open(file_path, "w") as f:#重新打开文件，选择写入模式
                    f.write(str_replace)      # 将修改后的字符串重新写入文件



str_substitute(folder_path='gpsindex',old_str=' ',new_str=',')
