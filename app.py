from flask import *
from flask_login import *
from models.portfolio import Portfolio
from models.mlab import *

app = Flask(__name__)
app.secret_key = "fD226QUKwZ5yta8yzFhpnmEdIfsbvmXjTc2qwkOn"

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
    return render_template("index.html", porfolios = Portfolio.objects)

if __name__ == '__main__':
    mlab_connect()
    app.run()


