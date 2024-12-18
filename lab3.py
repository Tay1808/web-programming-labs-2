from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'Неизвестный')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age', 'Не указан')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)
    
@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Tay', max_age=5)
    resp.set_cookie('age', '20', max_age=5)
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user = user, age=age, sex=sex, errors = errors)

@lab3.route('/lab3/order')
def order():
    return render_template('/lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0 
    drink = request.args.get('drink')

    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('/lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')  
    return render_template('/lab3/success.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    # Получаем значения из cookies или параметров запроса
    color = request.args.get('color')
    background = request.args.get('background')
    font_size = request.args.get('font_size')
    font_style = request.args.get('font_style')

    # Создаем ответ
    resp = make_response(redirect('/lab3/settings'))

    # Устанавливаем cookie для всех параметров, если они переданы
    if color:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color', color)
        return resp 
    
    if background:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('background', background)
        return resp 
    
    if font_size:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('font_size', font_size)
        return resp 
    
    if font_style:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('font_style', font_style)
        return resp 
   
    color = request.cookies.get('color')
    background = request.cookies.get('background')
    font_size = request.cookies.get('font_size')
    font_stylefont_style = request.cookies.get('font_style')
    resp = make_response(render_template('lab3/settings.html', color=color, background=background, font_size=font_size, font_style=font_style))

    return resp

@lab3.route('/lab3/clear_settings')
def clear_settings():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('background')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_weight')
    return resp

@lab3.route('/lab3/train_ticket')
def train_ticket():
    errors = {}
    price = 0

    # Получаем данные из формы через метод GET
    full_name = request.args.get('full_name')
    seat_type = request.args.get('seat_type')
    linen = request.args.get('linen')
    luggage = request.args.get('luggage')
    age = request.args.get('age')
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    travel_date = request.args.get('travel_date')
    insurance = request.args.get('insurance')

    # Валидация данных
    if full_name == '':
        errors['full_name'] = 'Введите ФИО!'
    if seat_type == '':
        errors['seat_type'] = 'Выберите тип полки!'
    if age == None:
        errors['age'] = ''
    elif age =='':
        errors['age'] = 'Заполните поле!'
    else:
        age = int(age)
        if age < 1 or age > 120:
            errors['age'] = 'Возраст должен быть от 1 до 120 лет!'
    if departure == '':
        errors['departure'] = 'Введите пункт выезда!'
    if destination == '':
        errors['destination'] = 'Введите пункт назначения!'
    if travel_date == '':
        errors['travel_date'] = 'Выберите дату поездки!'

    # Если ошибок нет, рассчитываем стоимость и показываем билет
    if not errors:
        age = int(age)
        if age < 18:
            price = 700  # Детский билет
            ticket_type = 'Детский билет'
        else:
            price = 1000  # Взрослый билет
            ticket_type = 'Взрослый билет'

        # Добавляем к стоимости за тип полки
        if seat_type in ['нижняя', 'нижняя боковая']:
            price += 100

        # Добавляем за бельё
        if linen == 'yes':
            price += 75

        # Добавляем за багаж
        if luggage == 'yes':
            price += 250

        # Добавляем за страховку
        if insurance == 'yes':
            price += 150

        # Формируем страницу с билетом
        return render_template('lab3/ticket.html', full_name=full_name, age=age, departure=departure,
                               destination=destination, travel_date=travel_date, ticket_type=ticket_type,
                               price=price)

    # Если есть ошибки, возвращаем форму с ошибками
    return render_template('lab3/train_ticket_form.html', errors=errors)

# Список товаров
products = [
    {'name': 'Chanel Classic Flap Bag', 'price': 5000, 'color': 'Black', 'brand': 'Chanel'},
    {'name': 'Louis Vuitton Neverfull', 'price': 1200, 'color': 'Brown', 'brand': 'Louis Vuitton'},
    {'name': 'Gucci Marmont Crossbody Bag', 'price': 1500, 'color': 'Pink', 'brand': 'Gucci'},
    {'name': 'Prada Saffiano Tote', 'price': 2400, 'color': 'Navy', 'brand': 'Prada'},
    {'name': 'Fendi Baguette Bag', 'price': 3000, 'color': 'Beige', 'brand': 'Fendi'},
    {'name': 'Dior Saddle Bag', 'price': 2000, 'color': 'Brown', 'brand': 'Dior'},
    {'name': 'Hermès Birkin Bag', 'price': 10000, 'color': 'Gold', 'brand': 'Hermès'},
    {'name': 'Burberry Monogram Banner Bag', 'price': 1500, 'color': 'Check', 'brand': 'Burberry'},
    {'name': 'Valentino Garavani Rockstud Bag', 'price': 2000, 'color': 'Red', 'brand': 'Valentino'},
    {'name': 'Michael Kors Jet Set Tote', 'price': 250, 'color': 'Black', 'brand': 'Michael Kors'},
    {'name': 'Tory Burch Perry Triple-Compartment Tote', 'price': 398, 'color': 'Bordeaux', 'brand': 'Tory Burch'},
    {'name': 'Céline Luggage Tote', 'price': 3500, 'color': 'Black', 'brand': 'Céline'},
    {'name': 'Chloé Drew Bag', 'price': 1900, 'color': 'Dusty Pink', 'brand': 'Chloé'},
    {'name': 'Guess Elana Shoulder Bag', 'price': 120, 'color': 'White', 'brand': 'Guess'},
    {'name': 'Kate Spade New York Margaret Tote', 'price': 298, 'color': 'Peach', 'brand': 'Kate Spade'},
    {'name': 'Marc Jacobs Snapshot Camera Bag', 'price': 350, 'color': 'Black', 'brand': 'Marc Jacobs'},
    {'name': 'Balenciaga City Bag', 'price': 2900, 'color': 'Black', 'brand': 'Balenciaga'},
    {'name': 'Off-White Diagonal Stripe Bag', 'price': 1300, 'color': 'Yellow', 'brand': 'Off-White'},
    {'name': 'Mansur Gavriel Bucket Bag', 'price': 495, 'color': 'Camel', 'brand': 'Mansur Gavriel'},
]


# Маршрут для отображения формы и поиска товаров
@lab3.route('/lab3/products')
def search_products():
    min_price = request.args.get('min_price', '')
    max_price = request.args.get('max_price', '')
    filtered_products = []

    # Фильтрация товаров по заданному диапазону цен
    if min_price.isdigit() and max_price.isdigit():
        min_price = int(min_price)
        max_price = int(max_price)
        filtered_products = [p for p in products if min_price <= p['price'] <= max_price]

    return render_template('lab3/products.html', products=filtered_products, min_price=min_price, max_price=max_price)