from flask import Flask, render_template, session, request, redirect
from datetime import datetime
app = Flask(__name__)
app.secret_key = "Kryptonian_Gold"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_money', methods = ['Post'])
def find_gold():
    return redirect('/')

app.run(debug=True)
