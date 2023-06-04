from flask import Blueprint, render_template

cnn = Blueprint(__name__, "cnn")

@cnn.route("/")
def home(): 
    return render_template("cnnPage.html")