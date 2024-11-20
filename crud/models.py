from dialogue.pretty import db

class Ais(db.Model):
    __tablename__ = "ais"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, index=True)
    kind = db.Column(db.String, index=True)
    count = db.Column(db.Integer)