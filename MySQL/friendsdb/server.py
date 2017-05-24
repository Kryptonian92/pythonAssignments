from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = "Kryptonian"
@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    print users
    return render_template('index.html')

@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')

# @app.route('/messages', methods=['POST'])
# def messeges():
#     if len(request.form['messages']) < 5:
#         flash('Invalid, has not been sent')
#     else:
#         flash('Valid, sending messege')
#         query = "INSERT INTO messages (messages, created_at, updated_at) VALUES (:messages, NOW(), NOW())"
#         data = {
#             'messages': request.form['messages']
#         }
#         mysql.query_db(query, data)
#     return redirect('/')


app.run(debug=True)
