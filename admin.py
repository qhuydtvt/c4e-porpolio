import datetime
from flask import *
from models.users import  User

import flask_login as login
import flask_admin
from mongoengine import *
from flask_admin.form import rules
from flask_admin.contrib.mongoengine import ModelView

# Define mongoengine documents

class Tag(Document):
    name = StringField(max_length=10)

    def __unicode__(self):
        return self.name


class Comment(EmbeddedDocument):
    name = StringField(max_length=20, required=True)
    value = StringField(max_length=20)
    tag = ReferenceField(Tag)


class Post(Document):
    name = StringField(max_length=20, required=True)
    value = StringField(max_length=20)
    inner = ListField(EmbeddedDocumentField(Comment))
    lols = ListField(StringField(max_length=20))


class File(Document):
    name = StringField(max_length=20)
    data = FileField()


class Image(Document):
    name = StringField(max_length=20)
    image = ImageField(thumbnail_size=(100, 100, True))


# Customized admin views
class UserView(ModelView):
    column_filters = ['email']

    column_searchable_list = ('email', 'password')

    form_ajax_refs = {
        'tags': {
            'fields': ('name',)
        }
    }

    def is_accessible(self):
        return login.current_user.is_authenticated

class PostView(ModelView):
    form_subdocuments = {
        'inner': {
            'form_subdocuments': {
                None: {
                    # Add <hr> at the end of the form
                    'form_rules': ('name', 'tag', 'value', rules.HTML('<hr>')),
                    'form_widget_args': {
                        'name': {
                            'style': 'color: red'
                        }
                    }
                }
            }
        }
    }

class AdminIndexView(flask_admin.AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated

#
# # Flask views
# @admin_page.route('/')
# def index():
# #     return '<a href="/admin/">Click me to get to Admin!</a>'
# def init_login(app):
#     login_manager = LoginManager()
#     login_manager.init_app(app)
#
#     @login_manager.user_loader
#     def load_user(email):
#         return User.objects(email=email).first()

def init(app):
    # Create admin
    admin = flask_admin.Admin(app, 'C4E-Portfolio', index_view=AdminIndexView())

    # Add views
    # admin.add_view(UserView(User))
    # admin.add_view(ModelView(Tag))
    # admin.add_view(PostView(Post))
    # admin.add_view(ModelView(File))
    # admin.add_view(ModelView(Image))


