import pandas as pd
from openpyxl import load_workbook

# 读取TDOC数据格式处理文件
file_path = '数据文件/TDOC数据格式.xlsx'
df = pd.read_excel(file_path)

# 定义多个坐标、长度和替换值，它们是一一对应的,默认第一行为列名，所以索引是从第二行第一列开始
positions = [int(df.iloc[1, 13]), int(df.iloc[1, 14]), int(df.iloc[1, 15]), int(df.iloc[1, 19])]  # 坐标列表，按需修改
lengths = [int(df.iloc[2, 13]), int(df.iloc[2, 14]), int(df.iloc[1, 15]), int(df.iloc[2, 19])]  # 长度列表，按需修改
replace_values = [
    '1',  # buyerInvoiceNo
    '2',  # blNo
    '3',  # blDate
    '5'   # invoiceNo
]

# 创建原始数据的副本
df_copy = df.copy()

# 获取原始数据
origin_data = df.iloc[9, 0]

# 切片获取需要替换的子串值
# initial_value = origin_data[position-1:position+length-1]

# 使用openpyxl来写入数据，并保留原始的公式或函数
wb = load_workbook('数据文件/TDOC数据格式.xlsx')
ws = wb.active


def process_data(position, lengths, replace_value):
    """
    替换原始数据中的值
    """
    if len(replace_value) <= lengths:
        replace_fix_value = replace_value.ljust(lengths)
    else:
        replace_fix_value = replace_value[:lengths]

    modified_data = origin_data[:position-1] + replace_fix_value + origin_data[position-1+lengths:]   # 将原有的子串值进行替换

    df_copy.iloc[9, 0] = modified_data  # 将处理后的数据写入副本的原始数据所在位置


for position, length, replace_value in zip(positions, lengths, replace_values):
    process_data(position, length, replace_value)

    # 获取修改后的数据
    modified_value = df_copy.iloc[9, 0]

    # 将修改后的数据写入到Excel文件中的对应单元格
    cell = ws.cell(row=12, column=1)
    cell.value = modified_value

    # 保存工作簿
    wb.save(file_path)

