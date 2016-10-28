from mongoengine import *
import flask_login

class User(Document):
    email = StringField()
    password = StringField()

def dump_user():
    for user in User.objects:
        user.delete()

class UserLogin(flask_login.UserMixin):
    def __init__(self, user):
        super(UserLogin, self).__init__()
        if user:
            self.id = user.email

    @classmethod
    def check(self, email, password):
        user = User.objects(email=email).first()
        if user :
            print("user not None")
            if(user.password == password):
                print("password valid")
                return UserLogin(user)
        return None

    @classmethod
    def get(cls, email):
        user = User.objects(email=email).first()
        if not user:
            print("User is None")
            return None
        print("User is not None")
        user_login = UserLogin(user)
        return user_login