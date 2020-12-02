from peewee import *

db = PostgresqlDatabase('contact_book', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db
class Contact(BaseModel):
    name = Charfield()
    phone = Numberfield()

