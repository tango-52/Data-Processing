import pandas as pd
from openpyxl import load_workbook

# 读取TDOC数据格式处理文件
file_path = '数据文件/TDOC数据格式.xlsx'
df = pd.read_excel(file_path)

# 获取位置信息, 默认第一行为列名，所以索引是从第二行第一列开始
position = df.iloc[1, 14]  # 获取B/L No位置信息
length = df.iloc[2, 14]  # 获取B/L No截取长度

print(type(position))
print(position)
print(type(length))

# 获取原始数据
origin_data = df.iloc[9, 0]

# 切片获取需要替换的子串值
initial_value = origin_data[position-1:position+length-1]

# 需要替换的值
replace_value = '828'
if len(replace_value) <= length:
    replace_fix_value = replace_value.ljust(length)
else:
    replace_fix_value = replace_value[:length]


# 将原有的子串值进行替换
modified_data = origin_data[:position-1] + replace_fix_value + origin_data[position-1+length:]

# 将处理后的数据写入原始数据所在位置
df.iloc[9, 0] = modified_data


# 将修改后的数据写入原始数据所在位置
df.iloc[9, 0] = modified_data

# 使用openpyxl来写入数据，并保留原始的公式或函数
wb = load_workbook('数据文件/TDOC数据格式.xlsx')
ws = wb.active

# 获取修改后的数据
modified_value = df.iloc[9, 0]

# 将修改后的数据写入到Excel文件中的对应单元格
cell = ws.cell(row=10, column=1)
cell.value = modified_value

# 保存工作簿
wb.save(file_path)
