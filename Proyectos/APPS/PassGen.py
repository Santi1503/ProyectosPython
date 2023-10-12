from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generatePass(length):
    char = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(char) for _ in range(length))
    return passw

@app.route('/')
def index():
    return render_template('../../Proyectos/templates/PassGen.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['longitud'])
    passw = generatePass(length)
    return render_template('../../Proyectos/templates/PassGen.html', passw=passw)

if __name__ == '__main__':
    app.run(debug=True)