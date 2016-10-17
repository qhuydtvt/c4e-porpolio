from mongoengine import *

class Student(Document):
    name = StringField()
    image = StringField()
    intro = StringField()
    role = StringField()