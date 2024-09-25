from flask import Flask, url_for, redirect,  render_template
app = Flask(__name__)

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


@app.route("/lab1/web")
def web():
    return '''<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href = "/lab1/author">author</a>
            </body> 
        </html>''', 200

@app.route("/lab1/author")
def author():
    name = "Лоринец Татьяна Андреевна"
    group = "ФБИ-22"
    faculty = "ФБ"

    return '''<!doctype html>
        <html>
            <body>
               <p>Студент: ''' + name + '''</p>
               <p>Группа: ''' + group + '''</p>
               <p>Факультет: ''' + faculty + '''</p>
               <a href = "/lab1/web">web</a>
            </body>
        </html>'''    


@app.route("/lab1/oak")
def oak():
    path = url_for("static", filename="oak.jpg")
    css = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel = "stylesheet" href="''' + css + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src = "''' + path + '''">
    </body>
</html>
'''
count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
    </body>
</html>
'''

@app.route('/lab1/clean_counter')
def clean_counter():
    global count
    count = 0  
    return '''
<!doctype html>
<html>
    <body>
        <h1>Счётчик очищен. Для перехода на страницу счетчитчика нажмите ниже.</h1>
        <a href="/lab1/counter">Вернуться на счетчик!</a>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return'''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>Что-то создано...</i></div>
    </body>
</html>
''', 201 

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
            </ul>
        </div>
        <footer>
            <p>Лоринец Татьяна Андреевна, ФБИ-22, 3 курс, 2024</p>
        </footer>
    </body>
</html>
'''

@app.route('/lab1')
def menu():
    return '''
<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
    </head>
    <body>
        <div>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div>   
        <a href="/">Назад</a> 
        <h2>Список роутов!</h2>
        <div>
            <ul>
                <li><a href="/lab1/web">WEB</a></li>
                <li><a href="/lab1/author">Author</a></li>
                <li><a href="/lab1/oak">Дуб</a></li>
                <li><a href="/lab1/counter">Cчетчик</a></li>
                <li><a href="/lab1/clean_counter">Очистка счетчика</a></li>
                <li><a href="/lab1/info">Информация</a></li>
                <li><a href="/lab1/created">Cоздание</a></li>
                <li><a href="/index">Меню</a></li>
                <li><a href="/lab1/cook">Кулинарных блог</a></li>
                <li><a href="/lab1/error_400">Ошибка 400</a></li>
                <li><a href="/lab1/error_401">Ошибка 401</a></li>
                <li><a href="/lab1/error_402">Ошибка 402</a></li>
                <li><a href="/lab1/error_403">Ошибка 403</a></li>
                <li><a href="/lab1/error_405">Ошибка 405</a></li>
                <li><a href="/lab1/error_418">Ошибка 418</a></li>
                <li><a href="/lab1/error_500">Ошибка 500</a></li>
            </ul>
        </div>
    </body>
</html>
'''

@app.route("/lab1/error_400")
def err400():
    return '''
<!doctype html>
<html>
    <body>
        <div>Некорректный запрос</div>
    </body>
</html>
''',  400

@app.route("/lab1/error_401")
def err401():
    return '''
<!doctype html>
<html>
    <body>
        <div>Ошибка авторизации</div>
    </body>
</html>
''',  401

@app.route("/lab1/error_402")
def err402():
    return '''
<!doctype html>
<html>
    <body>
        <div>Необходима оплата</div>
    </body>
</html>
''',  402

@app.route("/lab1/error_403")
def err403():
    return '''
<!doctype html>
<html>
    <body>
        <div>Недостаточно прав</div>
    </body>
</html>
''',  403

@app.route("/lab1/error_405")
def err405():
    return '''
<!doctype html>
<html>
    <body>
        <div>Не поддерживается.Неверный метод</div>
    </body>
</html>
''',  405

@app.route("/lab1/error_418")
def err418():
    return '''
<!doctype html>
<html>
    <body>
        <div>Я - чайник!</div>
        <div>Я не могу приготовить кофе!</div>
    </body>
</html>
''',  418

@app.route("/lab1/error_500")
def err500():
    res = 1/0 
    return(res)

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


@app.route("/lab1/cook")
def cooke():
    path = url_for("static", filename="cok.jpg")
    return '''
<!doctype html>
<html>
    <body>
        <div>Добрый день, дорогие подписочники!</div>
        <div>Я - Танюшка Хозяйка</div>
        <div>Cегодня мы будем готовить кексы!</div>
        <img src = "''' + path + '''">
        <div>Смешай все ингредиенты в одной большой миске, не забудь
        добавить щепотку оптимизма и стакан хорошего юмора. Выпекай их в заранее 
        разогретой духовке, пока не заполнится вся кухня чудесным пахнущим ароматом.</div>
        <div>Если на кухне дым и всё пошло не по плану, просто представь, что ты 
        создаёшь новый кулинарный тренд — "дымко-кулинария"! Включи вентилятор на полную мощность, 
        чтобы скрыть следы преступления, и постарайся выглядеть так, будто это было частью задумки</div?
        <div>Надеюсь у вас все получилось!</div>
        <div>Приятного аппетита вам и вашим близким!</div>
    </body>
</html>''', 200, {
    'Content-Launguage': 'ru',
    'X-DENDOBRI': 'Ivamtogogze',
    'X-Dosvidania': 'DoVstrech'
}

house_build = False 

@app.route('/lab1/resource')
def start_house():
    path = url_for("static", filename="travs.jpg")
    css = url_for("static", filename="err404.css")
    global house_build 
    status = "Дом построен" if house_build else "Дома еще нет!"
    response = f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css}">
    </head>
    <body>
        <h1>{status}</h1>
        <a href="/lab1/createdhouse">Построить дом</a><br>
        <a href="/lab1/delete">Снести дом</a><br>
        <img src = "''' + path + '''">
    </body>
</html>
'''
    return response, 200

@app.route('/lab1/createdhouse')
def build():
    css = url_for("static", filename="err404.css")
    path = url_for("static", filename="house.png")
    path1 = url_for("static", filename="house400.jpg")
    global house_build 
    if house_build :
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + css + '''">
        <style>
            img {
                width: 50%
                height:50%
            }
        </style>
    </head>
    <body>
        <h1>Дом уже есть. Сначала снесите то, что уже построено</h1>
        <a href="/lab1/resource">Назад</a><br>
        <img src = "''' + path1 + '''">
    </body>
</html>''', 400
    else:
        house_build = True 
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + css + '''">
        <style>
            img {
                width: 50%
            }
        </style>
    </head>
    <body>
        <h1>Отлично! Дом построен!</h1>
        <a href="/lab1/resource">Назад</a><br>
        <img src = "''' + path + '''">
    </body>
</html>''', 201
    
@app.route('/lab1/delete')
def delete_home():
    css = url_for("static", filename="err404.css")
    path = url_for("static", filename="delete.jpg")
    path1 = url_for("static", filename="delete.jpg")
    global house_build  
    if house_build:
        house_build = False 
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + css + '''">
        <style>
            img {
                width: 50%
            }
        </style>
    </head>
    <body>
        <h1>Красота! Дом снесен -  можно строить новый!</h1>
        <a href="/lab1/resource">Назад</a><br>
        <img src = "''' + path + '''">
    </body>
</html>''', 200
    else:
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + css + '''">
        <style>
            img {
                width: 50%
            }
        </style>
    </head>
    <body>
        <h1>Что тут сносить?! Нужно сначала что-то построить!</h1>
        <a href="/lab1/resource">Назад</a><br>
        <img src = "''' + path1 + '''">
    </body>
</html>
''', 400 


@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'пион', 'ромашка', 'лилия']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "Нет такого цветка", 404
    else:
        return "цветок: " + flower_list[flower_id]
    
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
<html>
'''

@app.route('/lab2/example')
def example():
    name = 'Танюшка Лоринец'
    numblab = '2'
    group = 'ФБИ-22'
    numbc = '3 курс'
    return render_template('example.html', name = name, numblab = numblab, group = group, numbc = numbc) 