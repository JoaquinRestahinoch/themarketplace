from flask import Flask, render_template, request, redirect, session
from productos import productos
from usuarios import usuarios_db, verificar_credenciales, crear_usuario

app = Flask(__name__, template_folder='templates')

@app.route('/')
def Index():
    return render_template('inicio.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/redireccionar', methods=['POST'])
def redireccionar():
    return redirect('/home.html')

@app.route('/categorias.html')
def categorias():
    return render_template('categorias.html')

@app.route('/category/<categoria>')
def category(categoria):
    productos_categoria = [producto for producto in productos if producto['categoria'] == categoria]
    return render_template('category.html', categoria=categoria, productos=productos_categoria)

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

@app.route('/terycond.html')
def terycond():
    return render_template('terycond.html')

@app.route('/productos/<int:producto_id>')
def mostrar_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        return render_template('productos.html', producto=producto)
    else:
        return "Producto no encontrado", 404

@app.route('/finalizacompra.html')
def fincompra():
    return render_template('finalizacompra.html')

@app.route('/quienessomos.html')
def quienessomos():
    return render_template('quienessomos.html')

@app.route('/defensaconsum.html')
def defconsum():
    return render_template('defensaconsum.html')

@app.route('/redireccionarr', methods=['POST'])
def redireccionarr():
    return redirect('/finalizacompra.html')

@app.route('/login.html')
def cargar_login():
    return render_template('login.html')

@app.route('/verificar_login', methods=['POST'])
def verificar_login():
    username = request.form['username']
    password = request.form['password']

    if verificar_credenciales(username, password):
        return redirect('/home.html')
    else:
        return "Credenciales incorrectas. Inténtalo de nuevo."

@app.route('/registro.html')
def cargar_registro():
    return render_template('registro.html')

@app.route('/crear_cuenta', methods=['POST'])
def crear_cuenta():
    username = request.form['username']
    password = request.form['password']

    if crear_usuario(username, password):
        return redirect('/login.html')
    else:
        return "El nombre de usuario ya está en uso. Inténtalo de nuevo."

if __name__ == '__main__':
    app.run(port=3000, debug=True)
