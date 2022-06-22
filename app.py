from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify
from models import db, LoanModel, AdminModel, productModel
from datetime import date

app = Flask(__name__)

app.secret_key = "secret-key"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    session['msg'] = ''
    session['authenticated'] = False
    db.create_all()
    return redirect(url_for('home'))


@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/dashboard', methods = ['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():

    message = session.get('msg')

    if request.method == 'POST':
        data = AdminModel.query.get(1)
        username = request.form['username']
        password = request.form['password']
        print(username + ' ' +password)

        if data.username == username and data.password == password:
            session['authenticated'] = True
            return redirect(url_for('dashboard'))
        else:
            session['msg'] = 'Invalid'
            return redirect(url_for('login', msg = message))


    return render_template('login.html', msg = message)




@app.route('/investment', methods = ['POST', 'GET'])
def investment():
    return render_template('investment.html')


@app.route('/loans_list', methods = ['POST', 'GET'])
def loans_list():
    loans = LoanModel.query.all()
    if request.method == 'GET':
        return render_template('loans_list.html', loans=loans)


    return render_template('loans_list.html')






@app.route('/inventory', methods = ['POST', 'GET'])
def inventory():

    products = productModel.query.all()
    if request.method == 'GET':
        return render_template('index.html', products=products)

    if request.method == 'POST':
        name = request.form['name']
        unitPrice = request.form['unitPrice']
        unitQuantity = request.form['unitQuantity']

        product = productModel(name,
                               unitPrice,
                               unitQuantity
                            )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('inventory'))

    return render_template('index.html')

@app.route('/update_inventory', methods = ['GET', 'POST'])
def update_inventory():
    if request.method == "POST":
        data = productModel.query.get(request.form.get('id'))
        data.name = request.form['name']
        data.unitPrice = request.form['unitPrice']
        data.unitQuantity = request.form['unitQuantity']

        db.session.commit()
        return redirect(url_for('inventory'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    data = productModel.query.get(id)
    db.session.delete(data)
    db.session.commit()
    flash("Profile Deleted!")
    return redirect(url_for('inventory'))

@app.route('/loan', methods = ['POST', 'GET'])
def loan():
    today = date.today()
    if request.method == 'POST':
        interest = 0
        penalty = 0
        month = 0

        fullname = request.form['fullname']
        birthdate = request.form['birthdate']
        p_number = request.form['p_number']
        email = request.form['email']
        address = request.form['address']
        e_name = request.form['e_name']
        purpose = request.form.get('p', False)
        loan_plan = request.form['loan_plan']
        amount = float(request.form['amount'])


        if loan_plan == '6 month/s [4%-3%]':
            interest = float(amount * .04)
            penalty = float(amount * .03)
            month = 6
        if loan_plan == '12 month/s [5%-3%]':
            interest = float(amount * .05)
            penalty = float(amount * .03)
            month = 12
        if loan_plan == '36 month/s [6%-3%]':
            interest = float(amount * .06)
            penalty = float(amount * .03)
            month = 36
        if loan_plan == '64 month/s [7%-2%]':
            interest = float(amount * .07)
            penalty = float(amount * .02)
            month = 64

        print(purpose)

        amount_payable = float(((amount / month) + interest) * month)
        monthly_payable = float(((amount / month) + interest))
        penalty = float((amount / month) + penalty + interest)

        loan = LoanModel(fullname,
                         birthdate,
                         p_number,
                         email,
                         address,
                         e_name,
                         today.strftime("%m/%d/%y"),
                         str(amount),
                         loan_plan,
                         purpose,
                         str(amount_payable),
                         str(monthly_payable),
                         str(penalty)
                         )
        db.session.add(loan)
        db.session.commit()
        return render_template('loan.html', ap = round(amount_payable,2), mp = round(monthly_payable,2), p = round(penalty,2))

    return render_template('loan.html')




if __name__ == '__main__':
    app.run(debug=True)
