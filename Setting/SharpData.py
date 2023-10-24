from Setting.date_process import *
from Setting.config import *


def process_data_for_file(filename, replace_values):
    # 获取positions、lengths等配置数据
    result_positions, result_lengths, data_locations, row_cols, file_path = conf_data(filename)

    # 读取需要处理的文件
    df = read_excel_file(file_path)
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

    return results, row_cols, file_path


# if __name__ == '__main__':
#     r = process_data_for_file()
#     print(r)