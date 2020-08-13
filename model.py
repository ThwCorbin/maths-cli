from peewee import *

db = PostgresqlDatabase('maths', user='postgres', password='', host='localhost', port=5432)

db.connect()

# Models
class BaseModel(Model):
	# A Meta class describes and configures another class
	class Meta:
		database = db

class Card(BaseModel):
	id = CharField()
	series = CharField()
	question = CharField()
	answer = CharField()
	correct = CharField()
	incorrect = CharField()

db.create_tables([Person, Pet])