from mongoengine import connect

db_name = "c4e-movie"
host = "ds057816.mlab.com"
port = 57816
username = "admin"
password = "admin"

def mlab_connect():
    connect(db=db_name, host=host, port=port, username=username, password=password)