from flask import Flask, render_template, redirect, request

app = Flask (__name__)

@app.route('/', methods =['GET', 'POST'])
def Name():
    return render_template('index.html')

@app.route("/results", methods=['GET', 'POST'])
def results():
    return render_template('results.html', name = request.form["name"], location = request.form["location"], language = request.form["language"], comments = request.form["description"])
    
app.run(debug=True)
