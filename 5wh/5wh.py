from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/ss', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        dirname = r'C:\Users\79194\PycharmProjects\Project_12.21\lessons\web\5wh\static\img'
        files = os.listdir(dirname)
        return render_template('5.1wh.html', title='carousel', files = files)
    elif request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(r'C:\Users\79194\PycharmProjects\Project_12.21\lessons\web\5wh\static\img', f.filename))
        # os.replace(f, "folder/renamed-text.txt")
        return 'Спасибо'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')