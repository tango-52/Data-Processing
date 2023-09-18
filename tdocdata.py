from date_process import *

config_file = 'tdoc_data_config.yaml'  # tdoc配置文件
config_data = read_config_file(config_file)  # 读取 YAML 配置文件

positions = config_data['positions']
lengths = config_data['lengths']
file_path = config_data['file_path']

df = read_excel_file(file_path)  # 读取需要处理的文件

replace_values = [
    '23',  # buyerInvoiceNo 长度15
    '23',  # blNo  长度20
    '23',  # blDate  长度8
    '23'   # invoiceNo  长度7
]
origin_data = df.iloc[9, 0]  # 获取原始数据


def process_data(position, lengths, replace_value, modified_data):
    """
    替换原始数据中的值
    """
    replace_fix_value = re_value(replace_value, lengths)
    modified_data = concat_value(modified_data, position, replace_fix_value, lengths)   # 将原有的子串值进行替换

    return modified_data


for position, length, replace_value in zip(positions, lengths, replace_values):
    origin_data = process_data(position, length, replace_value, origin_data)
    rewrite_excel(file_path, origin_data)

print(origin_data)


