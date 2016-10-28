from mongoengine import Document, StringField, ImageField

class Project(Document):
    title = StringField(max_length=20, required=True)
    description = StringField(max_length=100, required=True)
    image = ImageField(thumbnail_size=(100, 100, True))
    link = StringField(max_length=255, required=True)