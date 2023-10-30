from flask import Flask, render_template, request, redirect, url_for
import random
import string
import sqlite3

app = Flask(__name__)

# Configura la base de datos SQLite para contraseñas y un gestor
conn_passwords = sqlite3.connect('passwords.db')
conn_manager = sqlite3.connect('password_manager.db')
conn_passwords.execute('CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)')
conn_passwords.commit()
conn_manager.execute('CREATE TABLE IF NOT EXISTS password_manager (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)')
conn_manager.commit()

def generatePass(length):
    char = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(char) for _ in range(length))
    return passw

@app.route('/')
def index():
    return render_template('PassGen.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['longitud'])
    passw = generatePass(length)
    return render_template('PassGen.html', passw=passw)

@app.route('/add_password', methods=['POST'])
def add_password():
    name = request.form['name']
    password = request.form['password']

    # Almacena la contraseña en la base de datos de contraseñas
    conn_passwords = sqlite3.connect('passwords.db')
    cursor = conn_passwords.cursor()
    cursor.execute('INSERT INTO passwords (name, password) VALUES (?, ?)', (name, password))
    conn_passwords.commit()
    conn_passwords.close()

    return redirect(url_for('index'))

@app.route('/password_manager')
def password_manager():
    # Recupera contraseñas del gestor
    conn_manager = sqlite3.connect('password_manager.db')
    cursor = conn_manager.cursor()
    cursor.execute('SELECT * FROM password_manager')
    passwords_manager = cursor.fetchall()
    conn_manager.close()

    return render_template('password_manager.html', passwords_manager=passwords_manager)

@app.route('/add_password_manager', methods=['POST'])
def add_password_manager():
    name = request.form['name']
    password = request.form['password']

    # Almacena la contraseña en el gestor
    conn_manager = sqlite3.connect('password_manager.db')
    cursor = conn_manager.cursor()
    cursor.execute('INSERT INTO password_manager (name, password) VALUES (?, ?)', (name, password))
    conn_manager.commit()
    conn_manager.close()

    return redirect(url_for('password_manager'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5203, debug=True)
