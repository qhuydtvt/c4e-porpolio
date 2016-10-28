from flask import *
from models.portfolio import Portfolio
from models.mlab import *

app = Flask(__name__)
mlab_connect()

@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':

    app.run()


