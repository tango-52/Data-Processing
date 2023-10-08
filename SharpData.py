from date_process import *
from setting import *
from config import Configs


# cf = Configs()  # 传递正确的配置文件路径
# config_data = cf.read_config_file('Config/sharp_data_config.yaml')  # 读取 YAML 配置文件


# 获取positions、lengths等配置数据
result_positions, result_lengths, replace_values, data_locations, row_cols, file_path = conf_data('Config/sharp_data_config.yaml')

df = cf.read_excel_file(file_path)  # 读取需要处理的文件


# 将坐标和数据组合在一起
data_and_coordinates = zip(data_locations, result_positions, result_lengths, replace_values)

# 转换为列表
data_and_coordinates_list = list(data_and_coordinates)

# 创建一个空列表，用于存储每一组的最终结果
results = []

for (loc, row), positions_list, lengths_list, replace_value_list in data_and_coordinates_list:
    # 获取原始数据
    origin_data = df.iloc[loc, row]
    for position, length, replace_value in zip(positions_list, lengths_list, replace_value_list):
        # 处理数据并更新原始数据
        origin_data = process_data(position, length, replace_value, origin_data)

    # 将每一组的最终结果添加到结果列表中
    results.append(origin_data)

# 打印每一组的最终结果
for result, (row, column) in zip(results, row_cols):
    print(result)
    cf.rewrite_excel(file_path, result, row, column)
