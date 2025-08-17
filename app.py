from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template("index.html")

# Ruta dinámica con parámetro
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"Bienvenido, {nombre}!"

if __name__ == '__main__':
    app.run(debug=True)
