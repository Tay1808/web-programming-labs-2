from flask import Blueprint, url_for, redirect, render_template, request
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


# Список цветов и их цен
flower_list = [
    {'name': 'роза', 'price': 100},
    {'name': 'пион', 'price': 370},
    {'name': 'ромашка', 'price': 90},
    {'name': 'тюльпан', 'price': 240}
]


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return '''
        <html>
        <body>
            <h1>Ошибка 404</h1>
            <p>Такого цветка нет</p>
            <a href="/lab2/flowers">Вернуться ко всем цветам</a>
        </body>
        </html>
        ''', 404
    else:
        flower = flower_list[flower_id]
        return f'''
        <html>
        <body>
            <h1>Цветок: {flower['name']}</h1>
            <p>Цена: {flower['price']} руб.</p>
            <a href="/lab2/flowers">Вернуться ко всем цветам</a>
        </body>
        </html>
        '''


@lab2.route('/lab2/flowers')
def all_flowers():
    return render_template('lab2/flowers.html', flowers=flower_list)


@lab2.route('/lab2/delete_flower/<int:flower_id>', methods=['POST', 'GET'])
def delete_flower(flower_id):
    if flower_id >= len(flower_list):
        return '''
        <html>
        <body>
            <h1>Ошибка 404</h1>
            <p>Такого цветка нет</p>
            <a href="/lab2/flowers">Вернуться ко всем цветам</a>
        </body>
        </html>
        ''', 404
    else:
        flower_list.pop(flower_id)
        return redirect(url_for('lab2.all_flowers'))


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return '''
    <html>
    <body>
        <h1>Список цветов очищен</h1>
        <a href="/lab2/flowers">Вернуться ко всем цветам</a>
    </body>
    </html>
    '''


@lab2.route('/lab2/add_flower/', methods=['GET', 'POST'])
def add_flower():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        if not name or not price.isdigit():
            return '''
            <html>
            <body>
                <h1>Ошибка 400</h1>
                <p>Вы не задали имя цветка или цену</p>
                <a href="/lab2/flowers">Вернуться ко всем цветам</a>
            </body>
            </html>
            ''', 400
        else:
            flower_list.append({'name': name, 'price': int(price)})
            return redirect(url_for('lab2.all_flowers'))
    return '''
    <html>
    <body>
        <h1>Добавить новый цветок</h1>
        <form method="post">
            <label>Название цветка: <input type="text" name="name" required></label><br>
            <label>Цена цветка: <input type="number" name="price" required></label><br>
            <input type="submit" value="Добавить">
        </form>
        <a href="/lab2/flowers">Вернуться ко всем цветам</a>
    </body>
    </html>
    '''


@lab2.route('/lab2/example')
def example():
    name = 'Танюшка Лоринец'
    numblab = '2'
    group = 'ФБИ-22'
    numbc = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'персики', 'price': 170},
        {'name': 'апельсины', 'price': 120},
        {'name': 'манго', 'price': 350},
        {'name': 'киви', 'price': 230}
        ]
    return render_template('lab2/example.html', 
                           name = name, numblab = numblab, 
                           group = group, numbc = numbc,
                           fruits = fruits) 


@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)


@lab2.route('/lab2/calc')
def trasp():
    return redirect("/lab2/calc/1/1")


@lab2.route('/lab2/calc/<int:a>')
def redirect_calc(a):
    return redirect(url_for('operations', a=a, b=1))


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def operations(a, b):
    multiplication = a * b
    division = a / b if b != 0 else 'Ошибка: деление на ноль'
    addition = a + b
    subtraction = a - b
    exponentiation = a ** b

    return f'''
<!doctype html>
<html>
    <body>
    <h1>Расчет с параметрами:</h1>
    <p>Умножение: {a} * {b} = {multiplication}</p>
    <p>Деление: {a} / {b} = {division}</p>
    <p>Сложение: {a} + {b} = {addition}</p>
    <p>Вычитание: {a} - {b} = {subtraction}</p>
    <p>Возведение в степень: {a} <sup>{b}</sup> = {exponentiation}</p>
    </body>
</html>
'''

berries = [
    {
        'name': 'Клубника',
        'description': 'Сочная и сладкая ягода, идеально подходит для летних десертов.',
        'image': 'strawberry.jpg'
    },
    {
        'name': 'Малина',
        'description': 'Маленькая и ароматная ягода с насыщенным вкусом. Плоды, как правило, красного цвета, однако встречаются сорта желтой и даже черной малины.',
        'image': 'raspberry.jpg'
    },
    {
        'name': 'Черника',
        'description': 'Темная ягода, богатая антиоксидантами и полезна для зрения. Ягоды черники сочные, черные, с синевато-сизым налетом, блестящие. Мякоть темно-красная, сочная, мягкая, с множеством семян.',
        'image': 'blueberry.jpg'
    },
    {
        'name': 'Клюква',
        'description': 'Кисловатая ягода, часто используется для приготовления морсов и соусов. Цветёт клюква в июне, сбор ягод начинается в сентябре и продолжается всю осень.',
        'image': 'cranberry.jpg'
    },
    {
        'name': 'Арбуз',
        'description': 'Cамая большая ягода, используемая в самых различных областях от приготовления до творчества. Окраска арбуза коры от белой и жёлтой до тёмно-зелёной с рисунком в виде сетки, полос, пятен. Мякоть розовая, красная, малиновая, реже — белая и жёлтая.',
        'image': 'watermelon.jpg'
    }
]


@lab2.route('/lab2/berries/')
def show_berries():
    return render_template('lab2/berry.html', berries=berries)


books = [
    {"title": "Гарри Поттер и философский камень", "author": "Джоан Роулинг", "genre": "Фэнтези", "pages": 332},
    {"title": "Убить пересмешника", "author": "Харпер Ли", "genre": "Классика", "pages": 281},
    {"title": "Над пропастью во ржи", "author": "Джером Сэлинджер", "genre": "Классика", "pages": 277},
    {"title": "Властелин колец: Братство кольца", "author": "Дж. Р. Р. Толкин", "genre": "Фэнтези", "pages": 423},
    {"title": "451 градус по Фаренгейту", "author": "Рэй Брэдбери", "genre": "Научная фантастика", "pages": 256},
    {"title": "Большие надежды", "author": "Чарльз Диккенс", "genre": "Классика", "pages": 505},
    {"title": "Портрет Дориана Грея", "author": "Оскар Уайльд", "genre": "Роман", "pages": 304},
    {"title": "Зови меня своим именем", "author": "Андре Асиман", "genre": "Роман", "pages": 248},
    {"title": "Дюна", "author": "Фрэнк Герберт", "genre": "Научная фантастика", "pages": 412},
    {"title": "Маленькие женщины", "author": "Луиза Мэй Олкотт", "genre": "Классика", "pages": 759}
]


@lab2.route('/lab2/books/')
def book_list():
    return render_template('lab2/books.html', books=books)

