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


@app.route('/index/tdoc', methods=['GET', 'POST'])
def tdoc_edit():
    if request.method == 'GET':
        # 返回数据输入页面
        return render_template('tdoc_edit.html')
    if request.method == 'POST':
        # 返回数据生成结果
        replace_values = []
        filename_path = 'Config/tdoc_data_config.yaml'
        replace_value = request.form.getlist('tdoc[]')
        replace_values.append(replace_value)
        result = process_data(filename_path, replace_values)
        return render_template('tdoc_edit.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
