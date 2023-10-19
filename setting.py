from SharpData import process_data_for_file, rewrite_excel

if __name__ == '__main__':
    results, row_cols, file_path = process_data_for_file('Config/sharp_data_config.yaml')

    # 打印每一组的最终结果
    for result, (row, column) in zip(results, row_cols):
        print(result)
        rewrite_excel(file_path, result, row, column)
