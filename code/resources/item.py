from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank"
                        )

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item {} not found'.format(name)}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "You idiot, you made a duplicate item --> '{}'".format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except ItemModel.UnknownError:
            return{"message": "An error occurred inserting the item"}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': "Item '{}' deleted".format(name)}, 200
        return {'message': "Item {} not found".format(name)}, 400

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            try:
                item = ItemModel(name, **data)
            except ItemModel.UnknownError:
                return {'message': "Error adding item"}, 500
        else:
            try:
                item.price = data['price']
                item.store_id = data['store_id']
            except:
                return {'message': "Error updating item"}, 500
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return{'items': [item.json() for item in ItemModel.query.all()]}

    @jwt_required()
    def delete(self):
        if ItemModel.isEmpty():
            return {'message': 'no items fool'}
        else:
            for item in ItemModel.query.all():
                item.delete_from_db()
            return {'message': 'All Items Deleted :('}
