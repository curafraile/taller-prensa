import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuración para guardar imágenes subidas
UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegurar que la carpeta de descargas exista
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def archivo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Lista de noticias vacía para que no aparezca NADA por defecto
noticias = []

@app.route('/')
def inicio():
    return render_template('index.html', noticias=noticias)

# Ruta del panel de administración para subir noticias
@app.route('/admin')
def admin():
    return render_template('admin.html', noticias=noticias)

@app.route('/publicar', methods=['POST'])
def publicar():
    titulo = request.form.get('titulo')
    categoria = request.form.get('categoria')
    contenido = request.form.get('contenido')
    fecha = request.form.get('fecha')
    
    # Procesar la imagen si fue subida
    imagen_filename = None
    if 'imagen' in request.files:
        file = request.files['imagen']
        if file and file.filename != '' and archivo_permitido(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            imagen_filename = filename

    if titulo and contenido:
        noticias.insert(0, {
            'categoria': categoria if categoria else 'GENERAL',
            'titulo': titulo,
            'contenido': contenido,
            'fecha': fecha if fecha else 'Hoy',
            'imagen': imagen_filename
        })

    return redirect(url_for('inicio'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)