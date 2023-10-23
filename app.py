from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return

@app.route('/redireccionar', methods=['GET'])
def redireccionar():
    nombre = request.args.get('nombre')
    return redirect(url_for('saludo', nombre=nombre))


if __name__ == '__main__':
    app.run(debug=True)