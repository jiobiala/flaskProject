from flask import Flask, render_template, request, url_for, redirect, flash, session
from models import db, LoanModel, AdminModel
from datetime import datetime

app = Flask(__name__)

app.secret_key = "secret-key"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    session['authenticated'] = False
    db.create_all()
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/investment', methods = ['POST', 'GET'])
def investment():
    return render_template('base.html')

@app.route('/loan', methods = ['POST', 'GET'])
def loan():  # put application's code here
    amount_payable = 0
    monthly_payable = 0
    penalty = 0
    if request.method == 'POST':
        interest = 0
        penalty = 0
        month = 0

        loan_plan = request.form['loan_plan']
        amount = float(request.form['amount'])


        if loan_plan == '6 month/s [8%-3%]':
            interest = float(amount * .08)
            penalty = float(amount * .03)
            month = 6
        if loan_plan == '12 month/s [6%-3%]':
            interest = float(amount * .06)
            penalty = float(amount * .03)
            month = 12
        if loan_plan == '36 month/s [5%-3%]':
            interest = float(amount * .05)
            penalty = float(amount * .03)
            month = 36
        if loan_plan == '64 month/s [4%-2%]':
            interest = float(amount * .04)
            penalty = float(amount * .02)
            month = 64

        print(purpose)

        amount_payable = float(((amount / month) + interest) * month)
        monthly_payable = float(((amount / month) + interest))
        penalty = float((amount / month) + penalty + interest)
        return render_template('loan.html', ap = round(amount_payable,2), mp = round(monthly_payable,2), p = round(penalty,2))
    return render_template('loan.html')


if __name__ == '__main__':
    app.run(debug=True)
