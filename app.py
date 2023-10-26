from flask import Flask, render_template, request, redirect, url_for, session, jsonify
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

@app.route('/productos/<int:producto_id>')
def mostrar_product(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        return render_template('productos.html', producto=producto)
    else:
        return "Producto no encontrado", 404


@app.route('/products', methods=['GET', 'POST'])
def get_or_add_product():
    if request.method == 'GET':
        return jsonify(productos)
    elif request.method == 'POST':
        new_product = request.get_json()
        productos.append(new_product)
        return jsonify({'message': 'Producto agregado correctamente'})

@app.route('/products/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def get_update_or_delete_product(product_id):
    if request.method == 'GET':
        if product_id < 0 or product_id >= len(productos):
            return jsonify({'error': 'Producto no encontrado'}), 404
        return jsonify(productos[product_id])
    elif request.method == 'PUT':
        if product_id < 0 or product_id >= len(productos):
            return jsonify({'error': 'Producto no encontrado'}), 404
        updated_data = request.get_json()

        # Actualiza el producto manteniendo los datos existentes
        existing_product = productos[product_id]
        existing_product.update(updated_data)

        return jsonify({'message': 'Producto actualizado correctamente'})
    elif request.method == 'DELETE':
        if product_id < 0 or product_id >= len(productos):
            return jsonify({'error': 'Producto no encontrado'}), 404
        del productos[product_id]
        return jsonify({'message': 'Producto eliminado correctamente'})
    

@app.route('/search', methods=['GET'])
def search():
    termino_busqueda = request.args.get('q', '')

    resultado_busqueda = [producto for producto in productos if termino_busqueda.lower() in producto['name'].lower()]

    return render_template('resultado_busqueda.html', resultado_busqueda=resultado_busqueda, termino_busqueda=termino_busqueda)


if __name__ == '__main__':
    app.run(port=3000, debug=True)