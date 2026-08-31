from mongoengine import connect
from configure.settings import MONGODB_DB , MONGODB_URI

def connect_database():
    connect(db=MONGODB_DB,host=MONGODB_URI)