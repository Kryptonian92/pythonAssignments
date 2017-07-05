from flask import Flask, render_template, redirect, session, flash, request
app = Flask(__name__)
app.secret_key = "kryptonian"
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'wall_db')
import md5
import re

@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    print users
    print "***************"
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['email']) > 3:
        flash("Information Valid")
        query = "INSERT INTO  users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': request.form['password']
            # 'password': md5.new(request.form['password']).hexdigest()
        }

    else:
        flash("Information Is Invalid")

    return redirect("/")

@app.route('/postMessage/<id>', methods=['POST']) # this route will actually write the message to the database
def postMessage(id):
    query = "INSERT into messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
        "user_id": id,
        "message": request.form['message'],
    }
    mysql.query_db(query, data)
    return redirect("/demo")

@app.route('/demo') # just display the messages and form to post a message
def messages():
    query = "SELECT users.first_name, users.id AS user_id, messages.id AS message_id, messages.message FROM messages LEFT JOIN users ON messages.user_id = users.id;"
    messages = mysql.query_db(query)
    return render_template("the_wall.html", messages = messages)



app.run(debug=True)
