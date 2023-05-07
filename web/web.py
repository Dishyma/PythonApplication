from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'container2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

# Ruta para la página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el login
@app.route('/login', methods=['GET', 'POST'])
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

# Ruta para el registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']

        # Insertar el nuevo usuario en la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mysql.connection.commit()
        cur.close()

        # Redirigir al usuario a la página de login
        return redirect(url_for('login'))

    return render_template('register.html')

""" @app.route('/check')
def check_db_connection():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT 1')
        cur.close()
        return 'Conexión exitosa a la base de datos'
    except Exception as e:
        return 'Error al conectar a la base de datos'

@app.route('/list-tables')
def list_tables():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SHOW TABLES")
        tables = cur.fetchall()
        cur.close()
        
        table_list = [table[0] for table in tables]
        return f"Tablas de la base de datos: {', '.join(table_list)}"
    except Exception as e:
        return f'Error al obtener la lista de tablas: {str(e)}'

@app.route('/get-all-records')
def get_all_records():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM nombre_de_la_tabla")  # Reemplaza "nombre_de_la_tabla" con el nombre de tu tabla
        records = cur.fetchall()
        cur.close()
        
        # Construir una respuesta con los registros
        response = ""
        for record in records:
            response += f"ID: {record[0]}, Nombre: {record[1]}, OtroCampo: {record[2]}\n"  # Reemplaza los nombres de campo según tu tabla
        
        return response
    except Exception as e:
        return f'Error al obtener los registros: {str(e)}' """

# Ruta para el dashboard
@app.route('/dashboard')
def dashboard():
    return redirect('http://192.168.10.4:5600')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)