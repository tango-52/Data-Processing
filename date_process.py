from setting import *


# 判断替换value长度 进行截取或者补齐内容
def re_value(replace_value, lengths):
    # 将任何类型的数据都转换为字符串
    replace_value_str = str(replace_value)

    # 检查并处理字符串长度
    if len(replace_value_str) <= lengths:
        replace_fix_value = replace_value_str.ljust(lengths)
    else:
        replace_fix_value = replace_value_str[:lengths]

    return replace_fix_value


# 重新拼接数据
def concat_value(modified_data, position, replace_fix_value, lengths):
    modified_data = modified_data[:position - 1] + replace_fix_value \
                    + modified_data[position - 1 + lengths:]
    return modified_data


# 获取配置文件中的内容
def conf_data(config_file):
    config_data = handle_config(config_file)
    positions = config_data['positions']
    lengths = config_data['lengths']
    replace_values = config_data['replace_values']
    data_locations = config_data['data_locations']
    row_cols = config_data['row_cols']
    files = config_data['files']
    return positions, lengths, replace_values, data_locations, row_cols, files


#  替换原始数据
def process_data(position, lengths, replace_value, modified_data):
    replace_fix_value = re_value(replace_value, lengths)
    modified_data = concat_value(modified_data, position, replace_fix_value, lengths)  # 将原有的子串值进行替换

    return modified_data
