from mongoengine import *

class Portfolio(Document):
    title = StringField()
    image = StringField()
    description = StringField()