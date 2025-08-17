from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>¡Hola! Bienvenido a mi proyecto Flask 🚀</title>
        </head>
        <body>
            <h1>¡Hola! Bienvenido a mi proyecto Flask 🚀</h1>
            <p>Brayan Camacho</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
