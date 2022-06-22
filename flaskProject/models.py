from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class LoanModel(db.Model):
    __tablename__ = "loan"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200))
    name = db.Column(db.String(100))
    amount = db.Column(db.String(100), default=None)


    def __init__(self, date, name, amount):
        self.date = date
        self.name = name
        self.amount = amount



        def __repr__(self):
            return f"{self.name}"


class AdminModel(db.Model):
    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))


    def __init__(self, username, password):
        self.username = username
        self.password = password



        def __repr__(self):
            return f"{self.username}:{self.password}"