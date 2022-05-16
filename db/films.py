from peewee import (
    CharField, IntegerField)

from db import base


class FilmModel(base.BaseModel):

    order = IntegerField()
    value = CharField(50)
    title = CharField(50)