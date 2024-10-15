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
    resp.set_cookie('age', '20')
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

