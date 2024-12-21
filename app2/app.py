from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la conexión a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Ajusta según tu configuración
app.config['MYSQL_DB'] = 'RegistroAutos'

# Inicialización de MySQL
mysql = MySQL(app)

# Configuración secreta para mensajes flash
app.secret_key = 'mysecretkey'

# Ruta para listar autos
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM autos')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', autos=data)

# Ruta para agregar auto
@app.route('/add_auto', methods=['POST'])
def add_auto():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        anio = request.form['anio']
        precio = request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO autos (marca, modelo, anio, precio) VALUES (%s, %s, %s, %s)",
                    (marca, modelo, anio, precio))
        mysql.connection.commit()
        flash('Auto agregado correctamente')
        return redirect(url_for('index'))

# Ruta para eliminar auto
@app.route('/delete/<id>')
def delete_auto(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM autos WHERE id = %s', [id])
    mysql.connection.commit()
    flash('Auto eliminado correctamente')
    return redirect(url_for('index'))

# Ruta para editar auto
@app.route('/edit/<id>')
def edit_auto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM autos WHERE id = %s', [id])
    data = cur.fetchone()
    cur.close()
    return render_template('editar.html', auto=data)

@app.route('/update/<id>', methods=['POST'])
def update_auto(id):
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        anio = request.form['anio']
        precio = request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE autos
            SET marca = %s, modelo = %s, anio = %s, precio = %s
            WHERE id = %s
        """, (marca, modelo, anio, precio, id))
        mysql.connection.commit()
        flash('Auto actualizado correctamente')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
