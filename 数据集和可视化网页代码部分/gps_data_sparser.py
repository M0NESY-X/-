import pandas as pd

# 读取CSV文件
file_path = 'ALL_gps.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# 打印数据的前几行和列类型
print(data.head())
print(data.dtypes)

# 强制将经纬度列转换为数值类型，如果转换失败则设置为NaN
data['lat'] = pd.to_numeric(data['lat'], errors='coerce')
data['lng'] = pd.to_numeric(data['lng'], errors='coerce')

# 选择数值列
numeric_columns = data.select_dtypes(include=['number']).columns
data_numeric = data[numeric_columns]

# 按每20个点分组并计算均值
group_size = 500
data_grouped = data_numeric.groupby(data_numeric.index // group_size).mean()

# 选择经纬度列并保存结果
latitude_mean = data_grouped['lat']
longitude_mean = data_grouped['lng']

# 将经纬度均值组合成新的坐标列表
new_coordinates = list(zip(latitude_mean, longitude_mean))

# 将新的坐标列表转换为DataFrame
new_coordinates_df = pd.DataFrame(new_coordinates, columns=['lat', 'lng'])

# 显示前几行
print(new_coordinates_df)
new_coordinates_df.to_csv('sparse_points_modified1.csv',sep=',',index=False)