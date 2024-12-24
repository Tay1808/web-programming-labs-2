from flask import Blueprint, render_template, request, redirect, jsonify, session, current_app
from os import path
import sqlite3
import psycopg2
from psycopg2.extras import RealDictCursor
rgz = Blueprint('rgz',__name__)

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='tay_web_base',
            user='postgres',
            password='admin'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@rgz.route('/rgz/')
def main():
    if 'username' in session:
        login = True
    else:
        login = False

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM recipes")
    else:
        cur.execute("SELECT * FROM recipes")

    recipes = cur.fetchall()
    db_close(conn, cur)

    return render_template('rgz/menurgz.html', login=login, cookes=recipes)

@rgz.route('/rgz/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect('/rgz/')
        else:
            return render_template('rgz/login.html', error='Неверный логин или пароль')

    return render_template('rgz/login.html')

@rgz.route('/rgz/logout/')
def logout():
    session.pop('username', None)  # Удаляем пользователя из сессии

    # Получаем список рецептов из базы данных
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM recipes")
    else:
        cur.execute("SELECT * FROM recipes")
    recipes = cur.fetchall()
    db_close(conn, cur)

    return render_template('rgz/menurgz.html', login=False, cookes=recipes)

@rgz.route('/rgz/add_recipe/', methods=['GET', 'POST'])
def add_recipe():
    if 'username' not in session:
        return jsonify({'error': {'code': 1, 'message': 'Вы не авторизованы'}}), 401

    if request.method == 'POST':
        name = request.json.get('name')
        description = request.json.get('description')
        ingredients = request.json.get('ingredients')
        instructions = request.json.get('instructions')
        image_url = request.json.get('image_url')

        # Проверка на пустой URL изображения
        if not image_url:
            return jsonify({'error': {'code': 3, 'message': 'URL изображения обязателен'}}), 400

        # Проверка на заполнение обязательных полей
        if not name or not description or not ingredients or not instructions:
            return jsonify({'error': {'code': 2, 'message': 'Не все поля заполнены'}}), 400

        conn, cur = db_connect()

        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(
                "INSERT INTO recipes (name, description, ingredients, instructions, image_url) VALUES (%s, %s, %s, %s, %s)",
                (name, description, ingredients, instructions, image_url)
            )
        else:
            cur.execute(
                "INSERT INTO recipes (name, description, ingredients, instructions, image_url) VALUES (?, ?, ?, ?, ?)",
                (name, description, ingredients, instructions, image_url)
            )

        db_close(conn, cur)

        return jsonify({'result': 'Рецепт успешно добавлен'}), 200

    return render_template('rgz/add_recipe.html')

@rgz.route('/rgz/edit_recipe/<int:recipe_id>/', methods=['GET', 'POST'])
def edit_recipe(recipe_id):

    conn, cur = db_connect()

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        image_url = request.form.get('image_url')

        if not name or not description or not ingredients or not instructions:
            return jsonify({'error': {'code': 2, 'message': 'Не все поля заполнены'}}), 400

        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(
                "UPDATE recipes SET name=%s, description=%s, ingredients=%s, instructions=%s, image_url=%s WHERE id=%s",
                (name, description, ingredients, instructions, image_url, recipe_id)
            )
        else:
            cur.execute(
                "UPDATE recipes SET name=?, description=?, ingredients=?, instructions=?, image_url=? WHERE id=?",
                (name, description, ingredients, instructions, image_url, recipe_id)
            )

        db_close(conn, cur)

        return redirect('/rgz/')

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM recipes WHERE id=%s", (recipe_id,))
    else:
        cur.execute("SELECT * FROM recipes WHERE id=?", (recipe_id,))

    recipe = cur.fetchone()
    db_close(conn, cur)

    return render_template('rgz/edit_recipe.html', recipe=recipe)

@rgz.route('/rgz/delete_recipe/<int:recipe_id>/', methods=['POST'])
def delete_recipe(recipe_id):

    conn, cur = db_connect()

    try:
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("DELETE FROM recipes WHERE id=%s", (recipe_id,))
        else:
            cur.execute("DELETE FROM recipes WHERE id=?", (recipe_id,))

        db_close(conn, cur)
        return jsonify({'result': 'Рецепт успешно удален'}), 200
    except Exception as e:
        print(f"Ошибка при удалении рецепта: {e}")
        db_close(conn, cur)
        return jsonify({'error': {'code': 500, 'message': 'Ошибка сервера'}}), 500

@rgz.route('/rgz/search/', methods=['GET'])
def search_recipes():
    query = request.args.get('query', '')  # Получаем строку поиска (название рецепта)
    mode = request.args.get('mode', 'any')  # Режим поиска: 'any' (хотя бы один ингредиент) или 'all' (все ингредиенты)
    ingredients = request.args.get('ingredients', '').split(',')  # Получаем список ингредиентов

    # Убираем пустые элементы из списка ингредиентов
    ingredients = [ingredient.strip() for ingredient in ingredients if ingredient.strip()]

    conn, cur = db_connect()

    try:
        # Начальный запрос (по названию, если указано)
        sql_query = "SELECT * FROM recipes"
        params = []

        if query:
            sql_query += " WHERE name ILIKE %s" if current_app.config['DB_TYPE'] == 'postgres' else " WHERE name LIKE ?"
            params.append(f"%{query}%")

        # Добавляем условия по ингредиентам, если они указаны
        if ingredients:
            if query:  # Если уже есть WHERE, добавляем AND
                sql_query += " AND "
            else:
                sql_query += " WHERE "

            if mode == 'all':
                # Режим "все ингредиенты"
                for i, ingredient in enumerate(ingredients):
                    sql_query += f"ingredients ILIKE %s" if current_app.config['DB_TYPE'] == 'postgres' else "ingredients LIKE ?"
                    params.append(f"%{ingredient}%")
                    if i < len(ingredients) - 1:
                        sql_query += " AND "
            else:
                # Режим "хотя бы один ингредиент"
                sql_query += "("
                for i, ingredient in enumerate(ingredients):
                    sql_query += f"ingredients ILIKE %s" if current_app.config['DB_TYPE'] == 'postgres' else "ingredients LIKE ?"
                    params.append(f"%{ingredient}%")
                    if i < len(ingredients) - 1:
                        sql_query += " OR "
                sql_query += ")"

        # Выполняем запрос
        cur.execute(sql_query, tuple(params))
        recipes = cur.fetchall()

        db_close(conn, cur)
        return render_template('rgz/search_results.html', query=query, mode=mode, ingredients=ingredients, recipes=recipes)
    except Exception as e:
        print(f"Ошибка при поиске рецептов: {e}")
        db_close(conn, cur)
        return jsonify({'error': {'code': 500, 'message': 'Ошибка сервера'}}), 500