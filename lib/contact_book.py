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

# contact1= Contact(name='Mom', phone= '9045732670')
# contact1.save()
# # print("contact created")
# contact2= Contact(name='Taylane', phone= '9045555555')
# contact2.save()
# # print("contact created")
# contact3= Contact(name='Corey', phone= '4152406352')
# contact3.save()
# # print("contact created")
# contact4= Contact(name='Billy', phone= '9172253320')
# contact4.save()
# # print("contact created")
# contact5= Contact(name='Kira', phone= '9179722525')
# contact5.save()

hello2 = str(input("View Contact list"))
print("Contact list: ")

list_of_people = Contact.select()
print(list_of_people)
for people in list_of_people:
    print(people.name, people.phone)

# get
print("contact search" )
search= str(input("name: "))
get_contact = Contact.get(Contact.name == search)
print(get_contact.phone)

#update 
new_name=str(input(" update contact? "))
new_number= str(input(" input new number "))
print(type(new_number))
new_search= str(input("contact: "))
hello = Contact.get(Contact.name == new_search)

hello.phone = new_number
hello.save()
new_num= Contact.get()
print(hello)

#delete

list_of_people = Contact.select()
print(list_of_people)
for people in list_of_people:
    print(people.name, people.phone)
new_delete= str(input(" Delete Contact Name: "))

hello2 = Contact.get(Contact.name == new_delete)
hello2.delete_instance()
list_of_people = Contact.select()
print("Here is your new Contact list: ")
print(list_of_people)
for people in list_of_people:
    print(people.name, people.phone)

bye = (str("Contact Deleted"))
print(bye)
list_of_gente = Contact.select()
print("Updated List: ")
print(list_of_gente)
for gente in list_of_gente:
    print(gente.name, gente.phone)