from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

# Ruta para el login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']

        # Verificar si las credenciales son correctas
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            # Redirigir al usuario a otra ruta específica
            return redirect(url_for('dashboard'))
        else:
            # Mostrar un mensaje de error
            return render_template('login.html', error='Credenciales incorrectas')

    return render_template('login.html')

# Ruta para el dashboard
@app.route('/dashboard')
def dashboard():
    return 'Bienvenido al dashboard'

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=80)