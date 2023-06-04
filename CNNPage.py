from flask import Blueprint

knn = Blueprint(__name__, "cnn")

@knn.route("/")
def home(): 
    return "CNNPage"