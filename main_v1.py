#Estrutura inicial de un proyecto Flask
from flask import Flask

app = Flask(__name__)

# Indica cual es la raiz principal del proyecto
@app.route("/")

def index():
    return "<center><h1 style='color: blue;'>Hola desde flask</h1></center>"

"""
De esta manera, cada que se hagan cambios se tiene que 
reiniciar el servidor para reflejar los cambios
if __name__ == '__main__':
    app.run()
"""

#De esta no
if __name__ == '__main__':
    app.run(debug=True, port=8084)