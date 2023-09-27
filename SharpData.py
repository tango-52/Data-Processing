from date_process import *

config_file = 'Config/sharp_data_config.yaml'  # sharp配置文件
config_data = read_config_file(config_file)  # 读取 YAML 配置文件

file_path = config_data['file_path']

df = read_excel_file(file_path)  # 读取需要处理的文件

# origin_data = df.iloc[9, 0]  # 获取原始数据


result_positions, result_lengths, replace_values, data_locations = conf_data(config_data)  # 获取positions、lengths

# 将坐标和数据组合在一起
data_and_coordinates = zip(data_locations, result_positions, result_lengths, replace_values)

# 转换为列表
data_and_coordinates_list = list(data_and_coordinates)

for (loc, row), positions_list, lengths_list, replace_value_list in data_and_coordinates_list:
    # 获取原始数据
    origin_data = df.iloc[loc, row]
    # print(origin_data)
    for position, length, replace_value in zip(positions_list, lengths_list, replace_value_list):
        modified_data = process_data(position, length, replace_value, origin_data)

print(modified_data)

    # rewrite_excel(file_path, modified_data)
