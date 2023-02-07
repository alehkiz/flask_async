from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    idade = db.Column(db.Integer)
    
    def __repr__(self):
        return f'Test({self.name})'