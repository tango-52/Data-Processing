from flask import Flask, render_template, request
from run import process_data
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        filename_path = request.form.get('data_type')
        all_results = process_data(filename_path)  # 获取处理结果
        print(all_results)
        return render_template('index.html', all_results=all_results)

@app.route('/index/result', methods=['GET', 'POST'])
def result():



if __name__ == '__main__':
    app.run(debug=True)
