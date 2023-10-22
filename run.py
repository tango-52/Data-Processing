from Setting.SharpData import process_data_for_file, rewrite_excel

# if __name__ == '__main__':


def  process_data(filename_path):
    all_results = []
    # 选择需要处理的数据
    results, row_cols, file_path = process_data_for_file(filename_path)

    # 打印每一组的最终结果
    for result, (row, column) in zip(results, row_cols):
        rewrite_excel(file_path, result, row, column)
        all_results.append(result)

    return all_results
