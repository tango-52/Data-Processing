from flask import Flask, render_template, request
from run import process_data
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        filename_path = request.form.get('data_type')
        process_data(filename_path)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
