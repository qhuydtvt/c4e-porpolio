from flask import *
from movie import Movie
from mlab import *

app = Flask(__name__)
mlab_connect()

@app.route('/')
def index():
    return render_template("index.html", movies = Movie.objects)

if __name__ == '__main__':

    app.run()
    #
    # movie1 = Movie(title="Terminator", desc="Haha", img_link=TEST_IMG_LINK)
    # movie1.save()
    # movie2 = Movie(title="Fast & furious", desc="Hihi", img_link=TEST_IMG_LINK2)
    # movie2.save()

