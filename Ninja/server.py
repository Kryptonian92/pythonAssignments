from flask import Flask, render_template, redirect, request

app = Flask (__name__)

@app.route('/', methods =['GET', 'POST'])
def Name():
    return render_template('index.html')

@app.route('/ninja', methods =['GET', 'POST'])
def Ninja():
    return render_template('ninja.html')

@app.route("/ninja/<color>")
def ninja_color(color):
    if color == "blue":
        image_url = "/static/images/donatello.jpg"
    elif color == "purple":
        image_url = "/static/images/leonardo.jpg"
    elif color == "orange":
        image_url = "/static/images/michelangelo.jpg"
    # else color == "purple":
    #     image_url = "/static/images/leonardo.jpg"
    elif color == "red":
        image_url = "/static/images/raphael.jpg"
    else:
        image_url = "/static/images/notapril.jpg"
    return render_template('showninja.html', view_color = color, image_url = image_url)





app.run(debug=True)
