from flask import *
import flask_login

from models.mlab import *
from models.portfolio import *
from models.users import User
from models.projects import Project
import admin
import tempfile
import base64

app = Flask(__name__)
app.secret_key = "fD226QUKwZ5yta8yzFhpnmEdIfsbvmXjTc2qwkOn"
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
admin.init(app)
mlab_connect()

@app.route('/')
def index():
    return render_template("index.html", projects=Project.objects)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        form = request.form
        email = form["email"]
        password = form["password"]
        user = User.objects(email=email).first()
        if user:
            if user.password == password:
                flask_login.login_user(user)
                return redirect("/admin")
        return "Invalid credentials"

@app.route('/logout', methods=["GET", "POST"])
def logout():
    flask_login.logout_user()
    return redirect(url_for("index"))

@login_manager.user_loader
def user_loader(email):
    return User.objects(email=email).first()

@app.route("/project-image/<id>")
def get_image(id):
    project = Project.objects(id=id).first()
    image = project.image
    if image:
        return send_file(image, mimetype="image")
    else:
        return "404"

if __name__ == '__main__':

    app.run(port=5004)