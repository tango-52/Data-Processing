from flask import Flask, render_template, request, url_for, redirect
from run import process_data
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/index/data_edit', methods=['GET', 'POST'])
def data_edit():
    # 判断数据类型，重定向
    data_type = request.args.get('data_type')
    if data_type == 'tdoc':
        return redirect(url_for('tdoc_edit'))
    if data_type == 'sa':
        return redirect(url_for('sa_edit'))
    else:
        return render_template('index.html')


@app.route('/index/tdoc', methods=['GET', 'POST'])
def tdoc_edit():
    if request.method == 'GET':
        # 返回数据输入页面
        return render_template('tdoc_edit.html')
    if request.method == 'POST':
        # 返回数据生成结果
        filename_path = 'Config/tdoc_data_config.yaml'
        replace_value = request.form.getlist('tdoc[]')
        replace_values = [replace_value]
        result = process_data(filename_path, replace_values)
        return render_template('tdoc_edit.html', result=result)


@app.route('/index/sa', methods=['GET', 'POST'])
def sa_edit():
    if request.method == 'GET':
        # 返回数据输入页面
        return render_template('sa_edit.html')
    if request.method == 'POST':
        # 返回数据生成结果
        filename_path = 'Config/sharp_data_config.yaml'
        wa2 = request.form.getlist('wa2[]')
        wa3 = request.form.getlist('wa3[]')
        replace_values = [wa2, wa3]
        all_result = process_data(filename_path, replace_values)
        return render_template('sa_edit.html', all_result=all_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
