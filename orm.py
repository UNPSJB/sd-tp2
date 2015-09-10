from peewee import *

db = SqliteDatabase('db.db')

class Usuario(Model):
    name = CharField()
    email = CharField()
    # Ver como se guarda un blob

    class Meta:
        database = db

db.connect()
db.create_tables([Usuario], safe=True)



