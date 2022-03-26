from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/table_param/<sex>/<int:age>')
def table_param(sex, age):
    if sex == 'female' and age <= 21:
        return render_template('2whb.html',
                               title='rooms',
                               path_to_img=url_for("models",
                                                   filename="img/rozov.jpg"),
                               path_to_img_1=url_for("models",
                                                   filename="img/lil.jpg"))
    if sex == 'female' and age > 21:
        return render_template('2whb.html',
                               title='rooms',
                               path_to_img=url_for("models",
                                                   filename="img/krasn.jpg"),
                               path_to_img_1=url_for("models",
                                                 filename="img/big.jpg"))
    if sex == 'male' and age <= 21:
        return render_template('2whb.html',
                               title='rooms',
                               path_to_img=url_for("models",
                                                   filename="img/goluboi.jpg"),
                               path_to_img_1=url_for("models",
                                                     filename="img/lil.jpg"))
    if sex == 'male' and age > 21:
        return render_template('2whb.html',
                               title='rooms',
                               path_to_img=url_for("models",
                                                   filename="img/sine.jpg"),
                               path_to_img_1=url_for("models",
                                                     filename="img/big.jpg"))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')