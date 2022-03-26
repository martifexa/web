from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/astronaut_selection", methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="/static/css/style.css">
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Анкета претендента на участие в миссии</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="full_name" class="form-control" id="full_name" placeholder="Введите фамилию" name="full_name">
                                        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="studySelect">Какое у вас образование?</label>
                                            <select class="form-control" id="studySelect" name="study">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                              <option>Два высших</option>
                                            </select>
                                         </div>
                                         <label for="aboutSelect">Какие у вас есть профессии?</label>
                                         <div class="form-check">
                                             <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                             <label class="form-check-label" for="flexCheckDefault">
                                                 Инженер-исследователь
                                             </label>
                                         </div>
                                         <div class="form-check">
                                             <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                             <label class="form-check-label" for="flexCheckDefault">
                                                 Инженер-строитель
                                             </label>
                                         </div>
                                         <div class="form-check">
                                             <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                             <label class="form-check-label" for="flexCheckDefault">
                                                 Пилот
                                             </label>
                                         </div>
                                         <div class="form-check">
                                             <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                             <label class="form-check-label" for="flexCheckDefault">
                                                 Метеоролог
                                             </label>
                                         </div>
                                         <div class="form-check">
                                             <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                             <label class="form-check-label" for="flexCheckDefault">
                                                 Инженер по жизнеобеспечению
                                             </label>
                                         </div>
                                         <div class="form-check">
                                             <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                             <label class="form-check-label" for="flexCheckDefault">
                                                 Инженер по радиационной защите
                                             </label>
                                         </div>
                                         <div class="form-check">
                                             <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                             <label class="form-check-label" for="flexCheckDefault">
                                                 Врач
                                             </label>
                                         </div>
                                         <div class="form-check">
                                             <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                             <label class="form-check-label" for="flexCheckDefault">
                                                 Экзобиолог
                                             </label>
                                         </div>

                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['full_name'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['study'])
        print(request.form['about'])
        print(request.form['profession'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
