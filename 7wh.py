from flask import Flask, url_for

app = Flask(__name__)

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def promotion(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты отбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <div class="alert alert-primary" role="alert">
                      Претендента на участие в миссии { nickname }:
                    </div>
                    <div class="alert alert-secondary" role="alert">
                       Поздравляем!! Ваш рейтин после участия в { level } этапе отбора
                    </div>
                    <div class="alert alert-light" role="alert">
                      составляет { rating }
                    </div>
                    <div class="alert alert-warning" role="alert">
                        Желаем удачи!
                    </div>
                  </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')