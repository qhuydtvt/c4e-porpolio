from flask import *
from models.mlab import *
from models.portfolio import *

app = Flask(__name__)
mlab_connect()

@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    app.run()


