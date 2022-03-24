from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic')
    # Many to One relationship

    # lazy = 'dynamic'
    # this makes it so that stores are easy and inexpensive to create, however
    # there is a trade-off, in that calling json() will call a query every time

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

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
