from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "Kryptonian"

@app.route('/')
def counter():
    if "num" in session:
        session['num'] += 1
    else:
        session['num'] = 0
    return render_template('counter.html')

@app.route('/count', methods= ['post'])
def count():
    return redirect('/')

@app.route('/reset', methods = ['post'])
def reset():
    session['num'] = -1
    return redirect('/')
app.run(debug=True)
