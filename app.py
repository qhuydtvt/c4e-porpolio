from flask import *
import flask_login
from flask_login import *

from models.mlab import *
from models.portfolio import *
from models.users import *

app = Flask(__name__)
app.secret_key = "fD226QUKwZ5yta8yzFhpnmEdIfsbvmXjTc2qwkOn"
login_manager = LoginManager()
login_manager.init_app(app)
mlab_connect()

@app.route('/')
def index():
    return render_template("index.html", porfolios=Portfolio.objects)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        form = request.form
        email = form["email"]
        password = form["password"]
        user_login = UserLogin.check(email, password)
        if user_login:
            flask_login.login_user(user_login)
            return redirect(url_for("admin"))
        return "Invalid credentials"

@app.route('/logout', methods=["GET", "POST"])
def logout():
    flask_login.logout_user()
    return "Logged out"

@app.route('/admin')
@flask_login.login_required
def admin():
    return "admin"

@login_manager.user_loader
def user_loader(email):
    return UserLogin.get(email)

if __name__ == '__main__':
    app.run()


