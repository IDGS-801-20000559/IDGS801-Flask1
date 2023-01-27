#Estrutura inicial de un proyecto Flask
from flask import Flask

app = Flask(__name__)

# Indica cual es la raiz principal del proyecto
@app.route("/")
def index():
    return "<center><h1 style='color: blue;'>Hola desde flask</h1></center>"

@app.route("/hola")
def hola():
    return "<center><h1 style='color: gray;'>Hola desde hola</h1></center>"

@app.route("/nueva")
def nueva():
    return "<center><h1 style='color: purple;'>Hola desde nueva</h1></center>"

#De esta no
if __name__ == '__main__':
    app.run(debug=True, port=3000)