import requests

from db import models, films


URL = 'https://cinematica.kg/api/v1/movies/today'

def get_response_to_json(url):
    response = requests.get(url).json()
    return response


json_response = get_response_to_json(URL)['list']
film1 = json_response[0]['details']



class Film:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def get_info(self):
        return self.__dict__


# obj1 = Film(**film1[1])
# print(obj1.get_info())
# print(obj1.title)

# models.create_table()

# film_model1 = films.FilmModel(order = obj1.order, value = obj1.value, title = obj1.title)
# film_model1.save()
# films.FilmModel.create(order = 3, value = 'test3', title = 'test3')
# print(film_model1)

all_films = [Film(**film) for film in film1]

def create_film():
    for film in all_films:
        try:
            print(films.FilmModel.create(**film.get_info()))
        except Exception:
            print(film.get_info())
            continue

def get_films(sort: str = None):
    if sort is None:
        for film in films.FilmModel.select():
            print(film.id, film.order, film.title, film.value)
    else:
        if hasattr(films.FilmModel, sort):
            # filter = getattr(films.FilmModel, sort)
            for film in films.FilmModel.select().order_by(films.FilmModel.title):
                print(film.id, film.order, film.title, film.title)
        else: 
            raise ValueError('нету такого поля!!!')

def get_film(pk: int):
    film = films.FilmModel.get(films.FilmModel.id==pk)
    return {'id': film.id, 'title': film.title, 'value': film.value}
# get_films()
def delete_film(pk: int):
    try:
        film = films.FilmModel.get(films.FilmModel.id==pk)
    except Exception:
        print(f'object how to id:{pk} DoesNotExist')
    else:
        return film.delete_instance()

def update_film(pk: int, **kwargs):
    film = films.FilmModel.get(films.FilmModel.id==pk)
    film.title = kwargs.get('title', film.title)
    film.order = kwargs.get('order', film.order)
    film.value = kwargs.get('value', film.value)
    film.save()



get_films(sort = 'title')
# update_film(pk=4, title = 'new_test', order = 344)
# print(delete_film(pk=8)) 