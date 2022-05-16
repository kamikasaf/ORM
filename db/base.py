from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase('snake_film', user='erlan',password='246sqe',host='localhost',port=5432)

class BaseModel(Model):
    
    class Meta:
        database = db
