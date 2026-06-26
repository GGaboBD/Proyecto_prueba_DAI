from flask import Flask, jsonify, request

app = Flask(__name__)

productos = {
    101: {"codigo": 101, "nombre": "Teclado mecanico RGB", "precio": 45.00, "stock": 12}
}

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenidos al sistema",
        "version":"1.0",
        "endpoints": ["/productos","/productos/<id>"]
    })

@app.get("/productos")
def obtener_producto():
    return jsonify(list(productos.values()))