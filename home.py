from flask import Blueprint, render_template

homePage = Blueprint(__name__, "home")

@homePage.route('/knn')
def knn_route():
    return render_template("knnPage.html")

@homePage.route('/cnn')
def cnn_route():
    return render_template("cnnPage.html")

@homePage.route("/")
def home(): 
    return render_template("home.html")
