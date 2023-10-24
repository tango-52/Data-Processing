from Setting.SharpData import process_data_for_file, rewrite_excel


def process_data(filename_path, replace_values):
    all_results = []
    # 选择需要处理的数据
    results, row_cols, file_path = process_data_for_file(filename_path, replace_values)
    # 打印每一组的最终结果
    for result, (row, column) in zip(results, row_cols):
        rewrite_excel(file_path, result, row, column)
        all_results.append(result)

    return all_results

# if __name__ == '__main__':
#     r = process_data()
#     # print(r)