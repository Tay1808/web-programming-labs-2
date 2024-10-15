from flask import Flask, url_for, redirect,  render_template, request
from lab1 import lab1
from lab2 import lab2  
from lab3 import lab3

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)


@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="404err.png")
    css = url_for("static", filename="err404.css")
    return '''<!doctype html>
        <html>
            <head>
                <link rel = "stylesheet" href="''' + css + '''">
            </head>
            <body>
                <h1>Нет такой страницы. Ищите лучше!!</h1>
                <img src = "''' + path + '''">
            </body> 
        </html>''', 404


@app.route('/')
@app.route('/index')
def home():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>
        <div>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
                <li><a href="/lab2">Вторая лабораторная</a></li>
                <li><a href="/lab3">Третья лабораторная</a></li>
            </ul>
        </div>
        <footer>
            <p>Лоринец Татьяна Андреевна, ФБИ-22, 3 курс, 2024</p>
        </footer>
    </body>
</html>
'''

@app.errorhandler(500)
def error_500(err):
    return '''
<!doctype html>
<html>
    <body>
        <h1>!Внутренняя ошибка сервера!</h1>
        <div>
            Cервер столкнулся с внутренней проблемой и не может
            обработать отправленный запрос.
        </div>
        <div>
        Попробуйте повторить запрос позже или устраните ошибку приложения!
        </div>
    </body>
</html>
''',  500
