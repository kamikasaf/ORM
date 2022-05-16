from db import films, base


def create_table():
    print('connect database')
    base.db.connection()
    base.db.create_tables([films.FilmModel])

