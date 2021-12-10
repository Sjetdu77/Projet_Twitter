from __init__ import *
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prevision')
def prevision():
    return "Work in progress"

def DataManager(d: DataHandler = None, fr: FeatureRecipe = None, fe: FeatureExtractor = None):
    d = DataHandler()
    fr = FeatureRecipe(d)
    pass


#on appelera la fonction DataManager() de la facon suivante :
#X_train, X_test, y_train, y_test = DataManager()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
