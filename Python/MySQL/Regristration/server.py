from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SecretKey!"
mysql = MySQLConnector(app,'friendsdb')
import md5
import re

# email_regex =

@app.route('/')
def index():
    # email = mysql.query_db('SELECT LCASE(email) FROM customer')
    return render_template('index.html')

def new_user():
    query = "INSERT INTO friends (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    mysql.query_db(query,data)

@app.route('/process', methods=['POST'])
def results():
    flag = True # will remain True, if no errors were detected
    if not request.form("first_name") < 1:
        flag = False
    if not email_reges.match(request.form['email']):
        flag = False
        flash("your email is not valid")
    if len(request.form['password']) < 8:
            flash("your password must be 8 characers long")

    if flag:
        print "User info is good."
        query = "INSERT into users(first_name, last_name, email password, created_at,...) VALUES (:first_name, :last_name...)"
        data = {
            'first_name' = request.form['first_name']
            ..
            ..'password' = md5.new(request.form['password']).hexdigest()
        }
                request.session['user_id'] = msql.query_db(query, data)# store session loggind in user id
                return redirect("/success")
    else:
        print "User info had errors."
        return redirec("/")

@app.route("/success"):
def success():
query = "SELECT * from users where id = : user_id"
data{

}

@app.route("/login", methods = ['POST']):
def login():
    if len(request.form['email']) < 1 or len(request.form['password']) < 1:
        flash{messege}
    if not request.form['email'] and not request.form['password']: # fi either login field is blank redirect
        return redurect("/")
    else:
        #
        query = "SELECT * from users WHERE email = :email"
        data{
            'email': request.form['email']

        }
        user = mysql.query_db(query, data)
        print user
        if user:
            if user[0].password == hashed_form_password = md5.new(request.form['password']). hexdigest():
                session['user_id'] = user[0]['id']
            else:
                return redurect("/")
        else:
            return redurect("/")




    # if not request.form['first_name'].isalpha() or len(request.form['first_name']) <= 3:
    #     flash('First Name is not Valid')
    #     if not request.form['last_name'].isalpha() or len(request.form['last_name']) <=3:
    #         flash('Last Name is not Valid')
    #         if not request.form['password'] <=8:
    #             flash('Password Is not valid!')
    #             if not request.form['password'] <=8:
    #                 flash('Password Is not Valid!')
    # else:

    # f_name = request.form['first_name']
    # if not f_name > 3:
    #     flash("variable")
    # if request.form['first_name'].isalpha() and len(request.form['first_name']) > 3:
    #     flash('First Name is not Valid')
        # if not request.form['last_name'].isalpha() and len(request.form['last_name']) > 3:
        #     flash('Last Name is not Valid!')
            # if not request.form['email'].isalpha()
    # else:
        flash('Information Is Valid!')
        # new_user()





        # flash('First Name Is Valid!')
        # if request.form['last_name'].isalpha() and len(request.form['last_name']) > 3:
        #     flash('Last Name Is Valid!')
        #     if len(request.form['password']) > 8:
        #         flash('Password Is Valid!')
        #         if len(request.form['confirmation']) > 8:
        #             flash(' Confirmation Is Valid!')
        # new_user()
    # return redirect('/')


app.run(debug=True)








#
#
#
# from flask import Flask, request, redirect, render_template, flash, session
# from mysqlconnection import MySQLConnector
# app = Flask(__name__)
# app.secret_key = "SecretKey!"
# mysql = MySQLConnector(app,'friendsdb')
#
# @app.route('/')
# def index():
#     # email = mysql.query_db('SELECT LCASE(email) FROM customer')
#     return render_template('index.html')
#
# def new_user():
#     query = "INSERT INTO friends (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
#     data={
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email'],
#         'password': request.form['password']
#     }
#     mysql.query_db(query,data)
#
# @app.route('/process', methods=['POST'])
# def results():
#     if len(request.form['first_name']) > 3:
#         flash('First Name Is Not Valid!')
#         if len(request.form['last_name']) > 3:
#             flash('Last Name Is Not Valid!')
#             if len(request.form['password']) > 3:
#                 flash('Password Is Not Valid!')
#                 if len(request.form['confirmation']) > 6:
#                     flash(' Confirmation Is Not Valid!')
#
#     else:
#         new_user()
#         flash('Information Is Valid!')
#     return redirect('/')
#
#
# app.run(debug=True)
#
