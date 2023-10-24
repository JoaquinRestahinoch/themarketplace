usuarios_db = {
    'usuario1': 'contrasenia1',
    'usuario2': 'contrasenia2'
}

def verificar_credenciales(username, password):
    if username in usuarios_db and usuarios_db[username] == password:
        return True
    return False

def crear_usuario(username, password):
    if username in usuarios_db:
        return False
    usuarios_db[username] = password
    return True
