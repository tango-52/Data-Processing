from config import Configs as cf


# 读取yaml配置
def handle_config(config_file):
    config_data = cf.read_config_file(config_file)
    return config_data


# 获取Excel处理文件
# def file_path(config_file):
#     config_data = cf.read_config_file(config_file)
#     path = config_data['file']
#     return path

