from peewee import *

db = PostgresqlDatabase('contact', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db
        
class Contact(BaseModel):
    name = CharField()
    phone = CharField()

db.create_tables([Contact])

contact1= Contact(name='Mom', phone= '9045732670')
contact1.save()
# print("contact created")
contact2= Contact(name='Taylane', phone= '9045555555')
contact2.save()
# print("contact created")
contact3= Contact(name='Corey', phone= '4152406352')
contact3.save()
# print("contact created")
contact4= Contact(name='Billy', phone= '9172253320')
contact4.save()
# print("contact created")
contact5= Contact(name='Kira', phone= '9179722525')
contact5.save()

hello2 = str(input("Look at your list! Press enter to continue "))
print("Here is yourt list of contacts: ")

list_of_people = Contact.select()
print(list_of_people)
for people in list_of_people:
    print(people.name, people.phone)

# get
print("contact search" )
search= str(input("name: "))
get_contact = Contact.get(Contact.name == search)
print(get_contact.phone)

