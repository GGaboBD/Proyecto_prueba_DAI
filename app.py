
from flask import Flask, jsonify, request

app = Flask(__name__)

productos = {
    201: {"codigo": 201, "nombre": "Teclado mecanico RGB", "precio": 45.00, "stock": 12},
    202: {"codigo": 202, "nombre": "Mouse Inalambrico", "precio": 18.50, "stock": 25},
    203: {"codigo": 203, "nombre": 'Monitor LED 24"', "precio": 165.00, "stock": 8}
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

app.get("/productos/productos/<id>")
def obtener_productos(codigo):  
    producto = productos.get(codigo)
    if producto:
        return jsonify(producto)
    return jsonify({"mensaje": "Producto no encontrado"}), 404

@app.post("/productos")
def agregar_producto():
    nuevo_producto = request.get_json()
    if not nuevo_producto or "name" not in nuevo_producto:
        return jsonify
    
    codigo_producto = max(productos.keys(), default=100) + 1
    if codigo_producto in productos:
        return jsonify({"error": "Producto ya existe"}), 400

    nuevo_producto["codigo"] = codigo_producto
    productos[productos] = nuevo_producto
    return jsonify(nuevo_producto), 201

if __name__ == "__main__":
    app.run(debug=True)