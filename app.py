import os
import random
import string
from flask import Flask
from flask_restful import Api, reqparse
from pymongo import MongoClient

from api.records import RecordSearch

app = Flask(__name__)
api = Api(app)

# Debug mode is turned on but with prod mode it is ignored.
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)\
    for _ in range(50))

# Connection parameters are read from .env file
client = MongoClient(os.environ['MONGO_URI'])
db = client[os.environ['MONGO_DBNAME']]

# db is the pymongo cursor and it is passed to each endpoint, also the parser to read GET and POST parameters
api.add_resource(
    RecordSearch, '/suggestions/', resource_class_kwargs={'db' : db}
)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)