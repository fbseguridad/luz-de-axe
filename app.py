from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Simulación de base de datos (Luego puedes agregar cientos)
historias = {
    "maria-padilha": {"titulo": "Maria Padilha das Almas", "texto": "Historia larga aquí..."},
    "exu-caveira": {"titulo": "El Misterio de Exu Caveira", "texto": "Historia larga aquí..."}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historias')
def lista_historias():
    return render_template('lista.html', items=historias)

@app.route('/historia/<nombre>')
def ver_historia(nombre):
    datos = historias.get(nombre)
    return render_template('lectura.html', datos=datos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
