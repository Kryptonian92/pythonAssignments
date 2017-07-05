from flask import Flask, render_template
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'users')
# an example of running a query

query = ("INSERT into users (first_name, last_name, email, created_at, updated_at)
VAlUES (: FIRST_NAME, :LAST_NAME, )

data = {
    'first_name': "Ausar",
    'last_name': "Kim",
    "email": "email@site.com"
}

@app.route('/user')
def add_user():
    return render_template("form.html")



@app.route('/')
def index():
    print "test"
    query = ""*SELECT * from users"
    all_users = mysql.query_db(query)
    return render_template('index.html', all_users)
    print all_users

    for user in all_users:
print mysql.query_db(query, data)

app.run(debug=True)
