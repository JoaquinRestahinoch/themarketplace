from flask import Flask, render_template, request, redirect, url_for, session
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


if __name__ == '__main__':
    app.run(port=3000, debug=True)
