from date_process import *

config_file = 'Config/sharp_data_config.yaml'  # sharp配置文件
config_data = read_config_file(config_file)  # 读取 YAML 配置文件

file_path = config_data['file_path']

df = read_excel_file(file_path)  # 读取需要处理的文件

# origin_data = df.iloc[9, 0]  # 获取原始数据

result_positions, result_lengths, replace_values = conf_data(config_data)  # 获取positions、lengths


# 打印修改数据
def fix_val():
    for positions_list, lengths_list, replace_value_list in zip(result_positions, result_lengths, replace_values):
        for position, length, replace_value in zip(positions_list, lengths_list, replace_value_list):
            print(f'{position}-{length}-{replace_value}')
            # 更新变量以保存当前组合的值
            last_position = position
            last_length = length
            last_replace_value = replace_value
    # 在循环结束后，返回最后一个组合的值
    return last_position, last_length, last_replace_value



    # modified_data = process_data(position, length, replace_value, origin_data)

    # rewrite_excel(file_path, modified_data)

# print(modified_data)
