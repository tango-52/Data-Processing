import pandas as pd
from openpyxl import load_workbook

# 读取TDOC数据格式处理文件
file_path = '数据文件/TDOC数据格式.xlsx'
df = pd.read_excel(file_path)

# 定义多个坐标、长度和替换值，它们是一一对应的,默认第一行为列名，所以索引是从第二行第一列开始
positions = [int(df.iloc[1, 13]), int(df.iloc[1, 14]), int(df.iloc[1, 15]), int(df.iloc[1, 19])]  # 坐标列表，按需修改
lengths = [int(df.iloc[2, 13]), int(df.iloc[2, 14]), int(df.iloc[2, 15]), int(df.iloc[2, 19])]  # 长度列表，按需修改

replace_values = [
    '2',  # buyerInvoiceNo 长度15
    '3',  # blNo  长度20
    '4',  # blDate  长度8
    '6'   # invoiceNo  长度7
]

# 创建原始数据的副本
df_copy = df.copy()

# 获取原始数据
origin_data = df.iloc[9, 0]

# 使用openpyxl来写入数据，并保留原始的公式或函数
wb = load_workbook('数据文件/TDOC数据格式.xlsx')
ws = wb.active


def process_data(position, lengths, replace_value, modified_data):
    """
    替换原始数据中的值
    """
    if len(replace_value) <= lengths:
        replace_fix_value = replace_value.ljust(lengths)
    else:
        replace_fix_value = replace_value[:lengths]

    modified_data = modified_data[:position-1] + replace_fix_value + modified_data[position-1+lengths:]   # 将原有的子串值进行替换

    return modified_data


for position, length, replace_value in zip(positions, lengths, replace_values):
    origin_data = process_data(position, length, replace_value, origin_data)

# 将修改后的数据写入到Excel文件中的对应单元格
cell = ws.cell(row=12, column=1)
cell.value = origin_data

# 输出最终结果
print(origin_data)

# 保存工作簿
wb.save(file_path)
