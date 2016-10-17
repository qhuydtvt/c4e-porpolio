from mongoengine import  *
class Movie(Document):
    title = StringField()
    desc = StringField()
    img_link = StringField()
    rate = FloatField()

