from flask import Flask, render_template, request
from run import process_data
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/index/data_edit', methods=['GET', 'POST'])
def data_edit():
    FS = request.args.get('data_type')
    print(FS)
    if request.method == 'GET':
        return render_template('data_edit.html', FS=FS)
    if request.method == 'POST':
        data = request.form.getlist('tdoc[]')
        FS1 = request.form.get('data_type')
        print(FS)
        return render_template('data_edit.html', result=data, FS1=FS1)


if __name__ == '__main__':
    app.run(debug=True)
