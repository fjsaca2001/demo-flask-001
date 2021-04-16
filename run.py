"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask</h1>"

@app.route('/suma')
def suma():
    resultado = 10 + 10
    return "<h3>10 + 10 = %d</h3>" % (resultado)

@app.route('/listado')
def listado():
	return "<h1>Principales valles de la Provincia de Loja</h1><ul><li>Valle de Loja o de Cuxibamba, en la hoya de Zamora</li><li>Valle de Catamayo</li><li>Valle de Casanga</li><li>Valle de Malacatos</li><li>Valle de Vilcabamba</li><li>Valle de Piscobamba</li><li>Valle de Guancolla o el Ingenio</li><li>Valle de Sabiango</li><li>Valle de Puyango</li><li>Valle del rio Alamor</li></ul><h3>by @fjsaca2001</h3>"
	
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
