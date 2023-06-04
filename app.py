from flask import Flask
from CNNPage import knn;
from KNNPage import cnn;
from home import homePage;

app = Flask(__name__)

app.register_blueprint(knn, url_prefix = "/knn")
app.register_blueprint(cnn, url_prefix = "/cnn")
app.register_blueprint(homePage, url_prefix = "/")

if __name__ == '__main__':
    app.run()