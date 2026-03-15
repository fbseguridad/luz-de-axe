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

        # --- KIMBANDA (EL PODER DE LA NOCHE) ---
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
        },
        "exu-caveira-calunga": {
            "titulo": "Exu Caveira",
            "cat": "Kimbanda",
            "sub": "Señor de la Calunga",
            "contenido": "Rige sobre el cementerio. Corta las magias negras más pesadas y protege contra la muerte prematura.",
            "punto": "En la tumba donde vive, Caveira llegó a trabajar.",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },
        "exu-do-lodo": {
            "titulo": "Exu do Lodo",
            "cat": "Kimbanda",
            "sub": "Señor de los Pantanos",
            "contenido": "Entidad densa y poderosa. Se le pide para hundir a los enemigos y para limpiezas profundas de envidias antiguas.",
            "punto": "¡Salve Exu do Lodo, que camina donde nadie pisa!",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },
        "pomba-gira-cigana-pueblo": {
            "titulo": "Cigana de las Almas",
            "cat": "Gitanos",
            "sub": "Lectura de Destino",
            "contenido": "Trae el axé de las monedas y las barajas. Especialista en abrir la suerte financiera.",
            "punto": "¡Gana dinero, gana suerte, con la Cigana de las Almas!",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },

        # --- LÍNEAS DE TRABAJO (UMBANDA) ---
        "ze-pelintra-lira": {
            "titulo": "Seu Zé Pelintra",
            "cat": "Malandros",
            "sub": "Abogado de las Calles",
            "contenido": "Protector de los marginados. Ayuda en problemas con la justicia, juegos de azar y vicios.",
            "punto": "¡Zé Pelintra, Zé Pelintra, el rey de la bohemia!",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },
        "vovo-maria-conga": {
            "titulo": "Vovó Maria Conga",
            "cat": "Pretos Velhos",
            "sub": "Madre de la Sabiduría",
            "contenido": "Limpia el corazón de las personas tristes. Usa sus hierbas y su bendición para dar paz al hogar.",
            "punto": "¡Bendición, abuela! Trae el incienso para defumar.",
            "img": "https://i.imgur.com/vH1N5qj.jpeg"
        },
        "caboclo-7-matas": {
            "titulo": "Caboclo 7 Matas",
            "cat": "Caboclos",
            "sub": "Fuerza de la Selva",
            "contenido": "Experto en limpiezas de negocios. Trae la fuerza de los árboles para dar estabilidad económica.",
            "punto": "¡Eeee Caboclo, dueño de la mata virgen!",
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
        },
        "corte-envidia": {
            "titulo": "Limpieza con Exu Caveira",
            "resumen": "Quita el mal de ojo y las trabas espirituales.",
            "ritual": "Tierra de cementerio (un poco), sal gruesa y ruda..."
        }
    },
    "invitaciones": [
        {"templo": "Fiesta de Exu - Templo Las Almas", "img": "https://res.cloudinary.com/dv2316ai5/image/upload/v1710500000/invitacion1.jpg"},
        {"templo": "Sesión de Caridad - Umbanda Luz", "img": "https://res.cloudinary.com/dv2316ai5/image/upload/v1710500000/invitacion2.jpg"}
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

@app.route('/api/buzios')
def buzios():
    mensajes = [
        "Laroyé! Exu dice: Pon una ofrenda en la encrucijada y verás el milagro.",
        "Axé! La victoria llega por un camino que no esperas.",
        "Cuidado: Alguien cerca de ti está robando tu energía con envidia.",
        "Los Pretos Velhos dicen: Ten paciencia, el tiempo de Dios es perfecto.",
        "Zé Pelintra avisa: Cuidado con lo que firmas hoy."
    ]
    return jsonify({"mensaje": random.choice(mensajes)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
