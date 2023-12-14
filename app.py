# app.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Définir le chemin absolu du dossier des templates
template_folder = os.path.abspath('DEVOPS/templates')
app = Flask(__name__, template_folder=template_folder)

@app.route('/')
def accueil():
    return render_template('accueil.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)
