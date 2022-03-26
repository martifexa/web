from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/galery')
def carousel():
    return render_template('3.1wh.html', title='carousel')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')