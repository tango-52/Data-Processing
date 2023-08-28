import pandas as pd

# 读取tdoc数据格式处理文件
file_path = '数据文件/TDOC数据格式.xlsx'
df = pd.read_excel(file_path)

# 获取位置信息, 默认第一行为列名，所以索引是从第二行第一列开始
position = df.iloc[1, 14]  # 获取B/L No位置信息
length = df.iloc[2, 14]  # 获取B/L No截取长度

# 获取原始数据
origin_data = df.iloc[9, 0]
print(type(origin_data))
print(origin_data)

# 切片获取需要替换的子串值
initial_value = origin_data[position-1:position+length-1]

# 需要替换的值
replace_value = 't2345678901234567890123'
if len(replace_value) <= length:
    replace_fix_value = replace_value.ljust(length)
else:
    replace_fix_value = replace_value[:length]

print(len(replace_fix_value))
print(replace_fix_value)

# 将原有的子串值进行替换
modified_data = origin_data[:position-1] + replace_fix_value + origin_data[position-1+length:]
print(modified_data)


