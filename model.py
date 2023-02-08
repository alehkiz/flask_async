from core import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    _password = db.Column(db.String, nullable=False)
        
    def __repr__(self):
        return f'Test({self.name})'