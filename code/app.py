from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, UserList
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db
import logging


app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLACLCHEMY_TRACK_MODIFICATIONS'] = False
logging.basicConfig(level=logging.DEBUG)
app.secret_key = 'erik'
api = Api(app)
jwt = JWT(app, authenticate, identity)  # creates a new endpoint /auth


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
