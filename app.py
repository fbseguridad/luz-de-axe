from flask import Flask, render_template, abort, jsonify
import os
import random

app = Flask(__name__)

# --- GRAN BASE DE DATOS LUZ DE AXÉ ---
data = {
    "historias": {
        # --- ORIXÁS (LOS PADRES) ---
        "ogum": {
            "titulo": "Pai Ogum",
            "cat": "Orixá",
            "sub": "Señor de los Caminos y el Hierro",
            "contenido": "Ogum es el guerrero que vence las demandas. Dueño del hierro y las herramientas, es quien abre los caminos a sus hijos. Sin Ogum no hay batalla ganada.",
            "punto": "Ogum de Lei, no dejes a tus hijos caer...",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },
        "iemanja": {
            "titulo": "Mãe Iemanjá",
            "cat": "Orixá",
            "sub": "Reina del Mar",
            "contenido": "La madre de todos los Orixás. Su axé limpia el alma y trae armonía a la familia. Se le pide para la fertilidad y la paz mental.",
            "punto": "¡Odoyá! Reina de las olas, sálvanos con tu manto azul.",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },
        "oxossi": {
            "titulo": "Pai Oxóssi",
            "cat": "Orixá",
            "sub": "Rey de las Matas",
            "contenido": "El cazador de una sola flecha. Trae la abundancia, la comida y el conocimiento de las hierbas sagradas.",
            "punto": "¡Okê Arô! Cazador que vive en la selva virgen.",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },
        # --- KIMBANDA ---
        "tranca-ruas-almas": {
            "titulo": "Exu Tranca Ruas de las Almas",
            "cat": "Kimbanda",
            "sub": "Guardián de los Cruceros",
            "contenido": "Entidad de gran respeto. Tranca Ruas cuida los portales entre el mundo de los vivos y los muertos. Es justicia pura.",
            "punto": "¡Él es Tranca Ruas, el que vence en cualquier lugar!",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },
        "maria-padilha-7-encruzilhadas": {
            "titulo": "Maria Padilha 7 Encrucijadas",
            "cat": "Kimbanda",
            "sub": "Reina de la Seducción",
            "contenido": "La más buscada para amarres y retornos. Su poder en las encrucijadas no tiene límites cuando se trata de amor y dinero.",
            "punto": "¡Maria Padilha, reina de la 7 encrucijadas!",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        }
    },
    "conjuros": {
        "apertura-negocio": {
            "titulo": "Conjuro de Ogum para Clientes",
            "resumen": "Atrae prosperidad y abre las puertas de tu local.",
            "ritual": "Vela verde, granos de maíz y una espada de San Jorge..."
        },
        "retorno-amor": {
            "titulo": "Conjuro de Maria Padilha",
            "resumen": "Para que la persona amada regrese pidiendo perdón.",
            "ritual": "Miel, perfume de rosas y 7 velas rojas en círculo..."
        }
    },
    "invitaciones": [
        {"templo": "Fiesta de Exu - Templo Las Almas", "img": "https://res.cloudinary.com/dv2316ai5/image/upload/v1710500000/invitacion1.jpg"},
        {"templo": "Sesión de Caridad - Umbanda Luz", "img": "https://res.cloudinary.com/dv2316ai5/image/upload/v1710500000/invitacion2.jpg"}
    ],
    "cartas": [
        {"nombre": "La Fuerza (Ogum)", "mensaje": "Ogum dice: La victoria es tuya, pero debes actuar con coraje ahora.", "img": "https://i.imgur.com/vH1N5qj.jpeg"},
        {"nombre": "La Templanza (Iemanjá)", "mensaje": "Mãe Iemanjá te pide calma. Las aguas se calmarán.", "img": "https://i.imgur.com/vH1N5qj.jpeg"},
        {"nombre": "La Riqueza (Oxum)", "mensaje": "¡Ora iê iê ô! El oro entra a tu casa. Dinero inesperado llegará.", "img": "https://i.imgur.com/vH1N5qj.jpeg"},
        {"nombre": "El Destino (Tranca Ruas)", "mensaje": "Laroyé! Se cierra una puerta pero se abre un camino real.", "img": "https://i.imgur.com/vH1N5qj.jpeg"}
    ]
}

# --- RUTAS ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historias')
def lista_historias():
    return render_template('lista.html', items=data['historias'])

@app.route('/historia/<id>')
def lectura(id):
    post = data['historias'].get(id)
    if not post: abort(404)
    return render_template('lectura.html', post=post)

@app.route('/conjuros')
def lista_conjuros():
    return render_template('lista_conjuros.html', conjuros=data['conjuros'])

@app.route('/blog-invitaciones')
def blog():
    return render_template('blog.html', invitaciones=data['invitaciones'])

@app.route('/oraculo')
def oraculo():
    return render_template('oraculo.html')

@app.route('/tarot')
def tarot():
    return render_template('tarot.html')

# --- APIS (RETORNAN JSON) ---
@app.route('/api/buzios')
def buzios():
    mensajes = [
        "Laroyé! Exu dice: Pon una ofrenda en la encrucijada y verás el milagro.",
        "Axé! La victoria llega por un camino que no esperas.",
        "Cuidado: Alguien cerca de ti está robando tu energía.",
        "Los Pretos Velhos dicen: Ten paciencia, el tiempo de Dios es perfecto."
    ]
    return jsonify({"mensaje": random.choice(mensajes)})

@app.route('/api/carta')
def sacar_carta():
    return jsonify(random.choice(data["cartas"]))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
