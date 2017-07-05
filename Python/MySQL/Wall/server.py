from flask import Flask, render_template, redirect, session, flash, request
app = Flask(__name__)
app.secret_key = "churros"
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app, 'wall_db')
import md5
import re

# from mysqlconnection import MySQLconnector
import md5
import re

@app.route('/')
def index():
    print "***************"
    return render_template('index.html')

@app.route('/register', method = ['POST'])
def login():
    if len(request.form['email']) < 1:
        flash("Information Invalid")
    else:
        flash("Information Invalid")

    return redirect("/")



app.run(debug=True)
