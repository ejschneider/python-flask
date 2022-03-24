from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # Foreign Keys relate objects in databases to other objects
    # In the case of our current app, we know that if an item's store_id
    # is the same as a store's primary_key, the item belongs in that store

    # Additionally, SQLAlchemy is designed such that an object that has
    # other objects referencing it, cannot be deleted until all referenced
    # objects are deleted first
    store = db.relationship('StoreModel')
    # This is a JOIN

    # Every Item model has a property 'store' that is the store that
    # matches the store_id in its primary_key id

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # .query comes from SQLAlchemy
        # SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def isEmpty(cls):
        return cls.query.count() == 0

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
