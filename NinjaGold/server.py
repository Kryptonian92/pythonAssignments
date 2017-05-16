from flask import Flask, render_template, session, request, redirect
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = "Kryptonian_Gold"

@app.route('/')
def home():
    session['current_gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def find_gold():
    if(request.form ['building'] == 'farm'):
        x = random.randrange (10, 21)
        session['current_gold'] += x
        print x
        return render_template ('index.html', test = "CONGRATS!! You have earned", earned = "gold from the farm!!", golds = x, timestamp = datetime.now().replace(minute = 0))
    elif(request.form ['building'] == 'cave'):
        x = random.randrange (5, 11)
        session['current_gold'] += x
        print x
        return render_template ('index.html', test = "CONGRATS!! You have earned", earned = "gold from the Cave!!", golds = x, timestamp = datetime.now().replace(minute = 0))
    elif(request.form ['building'] == 'house'):
        x = random.randrange (2, 5)
        session['current_gold'] += x
        print x
        return render_template ('index.html', test = "CONGRATS!! You have earned", earned = "gold from the House!!", golds = x, timestamp = datetime.now().replace(minute = 0))
    elif(request.form ['building'] == 'casino'):
        x = random.randrange (0, 51)
        session['current_gold'] += x
        print x
        return render_template ('index.html', test = "CONGRATS!! You have earned", earned = "gold from the Casino!!", golds = x, timestamp = datetime.now().replace(minute = 0))
    @app.route('/reset', methods = ['POST'])
    def reset():
        # session['current_gold'] = 0
        return redirect('/')
app.run(debug=True)
