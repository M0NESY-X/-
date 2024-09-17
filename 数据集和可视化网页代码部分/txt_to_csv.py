import pandas as pd 
import os
def txt_to_csv(txt_file_path,csv_file_path): 
    # 读取txt文件
    # 使用pandas读取txt文件
    df = pd.read_csv(txt_file_path, sep=',')
   
    df.columns =['index','catagories','severity','drop']
    df.drop(columns = ['drop'],inplace = True)
    # 将数据写入csv文件
    df.to_csv(csv_file_path,sep=',', index=False)
    
    print(f"Successfully converted {txt_file_path} to {csv_file_path}.")

folder = 'gpsindex'

file_list = os.listdir(folder)
i = 1
for file in file_list:
    file_path = os.path.join(folder,file)
    new_file_path = os.path.join(folder,'gpsindex+label'+str(i)+'.csv')
    txt_to_csv(txt_file_path = file_path,csv_file_path=new_file_path)
    i = i + 1