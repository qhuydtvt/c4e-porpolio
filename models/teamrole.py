from mongoengine import *

class TeamRole(Document):
    title = StringField()
    code = StringField()