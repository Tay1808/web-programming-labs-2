from flask import Blueprint, render_template, request, redirect, session 
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('/lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='Невозможно совершить деление на ноль!')
    result = x1 / x2 
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 0

    if x2 == '':
        x2 = 0

    
    x1 = int(x1)
    x2 = int(x2)

    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/mult-form')
def mult_form():
    return render_template('lab4/mult-form.html')

@lab4.route('/lab4/mult', methods = ['POST'])
def mult():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 1

    if x2 == '':
        x2 = 1

    
    x1 = int(x1)
    x2 = int(x2)

    result = x1 * x2
    return render_template('lab4/mult.html', x1=x1, x2=x2, result=result)
 
@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods = ['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Ошибка! Нужно заполнить оба поля!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result) 

@lab4.route('/lab4/deg-form')
def deg_form():
    return render_template('lab4/deg-form.html')

@lab4.route('/lab4/deg', methods = ['POST'])
def deg():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/deg.html', error='Ошибка! Нужно заполнить оба поля!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0 and x1 == 0:
        return render_template('lab4/deg.html', error='Оба числа не могут быть 0!')
    result = x1 ** x2
    return render_template('lab4/deg.html', x1=x1, x2=x2, result=result) 


tree_count=0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count += 1 

    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Alexey Petrov', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Johnson', 'gender': 'male'},
    {'login': 'tay', 'password': '987', 'name': 'Taylor Swift', 'gender': 'female'},
    {'login': 'sofi', 'password': '666', 'name': 'Sofia Petrova', 'gender': 'female'},
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def  login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            user_name = ''
            for user in users:
                if user['login'] == login:
                    user_name = user['name']
                    break
              
           
        else:
            authorized = False
            login = ''
            user_name = ''

        return render_template("lab4/login.html", authorized = authorized, login = login, user_name = user_name)      
    
    login = request.form.get('login')
    password = request.form.get('password')

    # Проверка на пустые значения
    if login == '':
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    if password == '':
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    
    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
    
    error = 'Неверный логин и/или пароль'
    return render_template('lab4/login.html', error = error, authorized = False, login = login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')







