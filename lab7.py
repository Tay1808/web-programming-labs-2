from flask import Blueprint, render_template, request, redirect, session

lab7 = Blueprint('lab7',__name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')

films = [
    {
        "title": "Hachi: A Dog's Tale",
        "title_ru": "Хатико: Самый верный друг",
        "year": 2008,
        "description":"Однажды, возвращаясь с работы, профессор колледжа нашел на вокзале\
             симпатичного щенка породы акита-ину. Профессор и Хатико стали верными друзьями.\
            Каждый день пес провожал и встречал хозяина на вокзале."
    },
    {
        "title": "Titanic",
        "title_ru": "Титаник",
        "year": 1997,
        "description":"В первом и последнем плавании шикарного «Титаника»\
             встречаются двое. Пассажир нижней палубы Джек выиграл билет в\
             карты, а богатая наследница Роза отправляется в Америку, чтобы\
            выйти замуж по расчёту. Чувства молодых людей только успевают\
             расцвести, и даже не классовые различия создадут испытания влюблённым,\
             а айсберг, вставший на пути считавшегося непотопляемым лайнера."
    },
    {
        "title": "Home Alone",
        "title_ru": "Один дома",
        "year": 1990,
        "description":"Американское семейство отправляется из Чикаго в Европу,\
            но в спешке сборов бестолковые родители забывают дома... \
            одного из своих детей. Юное создание, однако, не теряется и демонстрирует чудеса\
            изобретательности. И когда в дом залезают грабители, им приходится не раз \
            пожалеть о встрече с милым крошкой."
    },
    {
        "title": "The Devil's Advocate",
        "title_ru": "Адвокат дьявола",
        "year": 1997,
        "description":"В Нью-Йорк по приглашению главы крупного юридического концерна\
            прибывает Кевин Ломакс, молодой адвокат. До этого он был известен тем, что защищал\
            исключительно негодяев и притом не проиграл ни одного процесса. На новом месте работы он\
            вполне счастлив, он живет в роскошной квартире с любящей женой, его окружают интересные люди."
    },
    {
        "title": "Avatar",
        "title_ru": "Аватар",
        "year": 2009,
        "description":"Бывший морпех Джейк Салли прикован к инвалидному креслу. Несмотря на немощное\
            тело, Джейк в душе по-прежнему остается воином. Он получает задание совершить путешествие в\
            несколько световых лет к базе землян на планете Пандора, где корпорации добывают редкий минерал,\
            имеющий огромное значение для выхода Земли из энергетического кризиса."
    },
]

@lab7.route('/lab7/rest-api/films/', methods = ['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        return "Film not found", 404
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        return "Film not found", 404
     
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        return "Film not found", 404
    
    film = request.get_json()
    films[id] = film
    return films[id]

@lab7.route('/lab7/rest-api/films/', methods = ['POST'])
def add_film():
     
    film = request.get_json()
    films.append(film)
    new_film_index = len(films) - 1
    return {"index": new_film_index}, 201