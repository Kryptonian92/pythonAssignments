from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SecretKey!"
mysql = MySQLConnector(app,'sakila')

@app.route('/')
def index():
    # email = mysql.query_db('SELECT LCASE(email) FROM customer')
    return render_template('index.html')

def new_email():
    query = "INSERT INTO new_emails (email, created_at) VALUES (:email, NOW())"
    data={
        'email': request.form['email_form']
    }
    mysql.query_db(query,data)


@app.route('/email_processing', methods=['POST'])
def results():
    email = mysql.query_db('SELECT LCASE(email) FROM customer')
    print email

    if {'LCASE(email)' :request.form['email_form']} in email:
        flash('Email address you entered is a VALID email address! Thank You!')
        new_email()
        added_emails = mysql.query_db ('SELECT * FROM new_emails')

        return render_template('success.html', new_email = added_emails)
    else:
        new_email()
        flash('Email Is Not Valid!')
    return redirect('/')
    
app.run(debug=True)
