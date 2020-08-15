from peewee import *

db = PostgresqlDatabase('maths', user='postgres', password='', host='localhost', port=5432)

db.connect()

# Models
# Create a base model class which specifies our database
class BaseModel(Model):
	# Meta class describes and configures another class
	class Meta:
		database = db

# Flash card model
class Card(BaseModel):
	# PeeWee creates primary key named “id”
	series = IntegerField()
	question = CharField()
	answer = CharField()

db.create_tables([Card])