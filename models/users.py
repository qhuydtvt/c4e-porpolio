from mongoengine import *

class User(Document):
    email = StringField(max_length=40)
    tags = ListField(ReferenceField('Tag'))
    password = StringField(max_length=40)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    def __unicode__(self):
        return self.email
