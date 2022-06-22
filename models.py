from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class productModel(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    unitPrice = db.Column(db.String(200))
    unitQuantity = db.Column(db.String(200))

    def __init__(self, name, unitPrice, unitQuantity):
        self.name = name
        self.unitPrice = unitPrice
        self.unitQuantity = unitQuantity

        def __repr__(self):
            return f"{self.name}"



class LoanModel(db.Model):
    __tablename__ = "loan"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(200))
    birthdate = db.Column(db.String(200))
    p_number = db.Column(db.String(200))
    email = db.Column(db.String(200))
    address = db.Column(db.String(200))
    e_name = db.Column(db.String(200))
    date = db.Column(db.String(200))
    amount = db.Column(db.String(100), default=None)
    loan_plan = db.Column(db.String(100), default=None)
    purpose = db.Column(db.String(100))
    ap = db.Column(db.String(100), default=None)
    mp = db.Column(db.String(100), default=None)
    p = db.Column(db.String(100), default=None)

    def __init__(self, fullname, birthdate, p_number, email, address, e_name, date, amount, loan_plan, purpose, ap, mp, p):
        self.fullname = fullname
        self.birthdate = birthdate
        self.p_number = p_number
        self.email = email
        self.address = address
        self.e_name = e_name
        self.date = date
        self.amount = amount
        self.loan_plan = loan_plan
        self.purpose = purpose
        self.ap = ap
        self.mp = mp
        self.p = p


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