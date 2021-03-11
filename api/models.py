
from extensions import db


class Db(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    designation = db.Column(db.String())
    full_name = db.Column(db.String())
    assembly = db.Column(db.String())
    district = db.Column(db.String())
    phone_no = db.Column(db.String())
    email = db.Column(db.String())
    gender = db.Column(db.String())

    @ classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
