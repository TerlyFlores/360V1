import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'PayDeManzana$'
app.config['MYSQL_DB'] = 'tour_virtual'
mysql = MySQL(app)

# Carpeta donde están las imágenes
IMAGES_FOLDER = 'static/images'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    codigo = request.form['codigo']
    contraseña = request.form['contraseña']
    
    # Validación de credenciales
    if codigo == "A002" and contraseña == "contraseña456":
        session['user_id'] = codigo
        return redirect(url_for('dashboard'))
    elif codigo == "A001" and contraseña == "contraseña123":
        session['user_id'] = codigo
        return redirect(url_for('course'))  # Redirige a course directamente para A001
    else:
        return "Usuario o contraseña incorrectos", 401

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/admin_utp360')
def admin_utp360():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    
    imagenes = os.listdir(IMAGES_FOLDER)
    imagenes = [img for img in imagenes if img.endswith('.jpg')]  

    return render_template('admin_utp360.html', imagenes=imagenes)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.png'):
       
        file.save(os.path.join(IMAGES_FOLDER, file.filename))
        return redirect(url_for('admin_utp360'))

@app.route('/delete_image', methods=['POST'])
def delete_image():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    image_name = request.form['image_name']
    try:
        os.remove(os.path.join(IMAGES_FOLDER, image_name))
        return redirect(url_for('admin_utp360'))
    except FileNotFoundError:
        return "Imagen no encontrada", 404

@app.route('/rename_image', methods=['POST'])
def rename_image():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    old_name = request.form['old_name']
    new_name = request.form['new_name'] + ".png"
    
    try:
        os.rename(os.path.join(IMAGES_FOLDER, old_name), os.path.join(IMAGES_FOLDER, new_name))
        return redirect(url_for('admin_utp360'))
    except FileNotFoundError:
        return "Imagen no encontrada", 404


@app.route('/course')
def course():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('course.html')

@app.route('/scan_qr')
def scan_qr():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('scan_qr.html')


@app.route('/process_qr', methods=['POST'])
def process_qr():
    data = request.get_json()
    aula_id = data.get('aula_id')

 
    if aula_id == 'valid_code':  
        image_path = 'path/to/image.jpg'  
        return jsonify({'status': 'success', 'image_path': image_path})
    else:
        return jsonify({'status': 'error'})


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/viewer')
def viewer():
    image_path = request.args.get('image_path')  
    if image_path:
        
        image_file = image_path  
        print(f"Intentando cargar la imagen desde: {image_file}")

       
        if os.path.exists(os.path.join('static', 'images', f'{image_file}.jpg')):
            return render_template('viewer.html', image_path=image_file)
        else:
            return render_template('error.html', error_message="Imagen no encontrada.")
    else:
        return render_template('error.html', error_message="No se proporcionó un nombre de imagen.")


@app.route('/course')
def next_page():
    
    return render_template('course.html') 

if __name__ == '__main__':
    app.run(debug=True)
