import os
from flask import Flask, render_template

app = Flask(__name__)

# Noticias base de la Prensa Técnico-Estudiantil
noticias = [
    {
        'categoria': 'DESAFÍO ECO / EVENTOS',
        'titulo': 'Bienvenidos al Medio Digital del Taller',
        'contenido': 'Este es el portal propio desarrollado en Python para cubrir las actividades, carreras y proyectos del taller.',
        'fecha': '29/07/2026'
    }
]

@app.route('/')
def inicio():
    return render_template('index.html', noticias=noticias)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)