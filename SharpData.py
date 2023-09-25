from date_process import *

config_file = 'Config/sharp_data_config.yaml'  # sharp配置文件
config_data = read_config_file(config_file)  # 读取 YAML 配置文件

file_path = config_data['file_path']

df = read_excel_file(file_path)  # 读取需要处理的文件

replace_values = [
    '23',  # buyerInvoiceNo 长度15
    '23',  # blNo  长度20
    '23',  # blDate  长度8
    '23'   # invoiceNo  长度7
]
# origin_data = df.iloc[9, 0]  # 获取原始数据


def process_data(position, lengths, replace_value, modified_data):
    """
    替换原始数据中的值
    """
    replace_fix_value = re_value(replace_value, lengths)
    modified_data = concat_value(modified_data, position, replace_fix_value, lengths)   # 将原有的子串值进行替换

    return modified_data


def fanhui():
    for datatype in config_data:
        if datatype == 'positions':
            positions = config_data[datatype]
        elif datatype == 'lengths':
            lengths = config_data[datatype]

    # 在循环结束后返回 positions 和 lengths
    return positions, lengths


result_positions, result_lengths = fanhui()
# print(result_positions, result_lengths)


for positions_list, lengths_list in zip(result_positions, result_lengths):
    print(positions_list)
    for position, length in zip(positions_list, lengths_list):
        print(f"Position: {position}, Length: {length}")
# 现在你可以使用 result_positions 和 result_lengths 这两个变量
# for position, length in zip(positions, lengths):
    #     print(position)

        # origin_data = process_data(position, length, replace_value, origin_data)
        # rewrite_excel(file_path, origin_data)

# print(origin_data)


