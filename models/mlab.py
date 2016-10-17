from mongoengine import connect

db_name = "c4e-portfolio"
host = "ds059516.mlab.com"
port = 59516
username = "admin"
password = "admin"

db_instance = None

def mlab_connect():
    global db_instance
    db_instance = connect(db=db_name, host=host, port=port, username=username, password=password)

def mlab_disconnect():
    db_instance.close()