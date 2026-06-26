import requests

BASE_URL = "http://127.0.0.1:5000/productos"

def consultar_catalogo():
    print("\n--- 1. Consultando el Catálogo Completo ---")
    try:
        response = requests.get(BASE_URL)
        print(f"Estado HTTP: {response.status_code}")
        print("Respuesta del servidor:")
        print(response.json())
    except Exception as e:
        print(f"Error de conexión: {e}")

def consultar_producto_especifico(codigo):
    print(f"\n--- 2. Consultando Producto con Código: {codigo} ---")
    try:
        response = requests.get(f"{BASE_URL}/{codigo}")
        print(f"Estado HTTP: {response.status_code}")
        print("Respuesta del servidor:")
        print(response.json())
    except Exception as e:
        print(f"Error de conexión: {e}")

def registrar_nuevo_producto(nombre, precio, stock):
    print(f"\n--- 3. Registrando Nuevo Producto: {nombre} ---")

    payload = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    try:
        response = requests.post(BASE_URL, json=payload)
        print(f"Estado HTTP: {response.status_code}")
        print("Respuesta del servidor:")
        print(response.json())
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":

    consultar_catalogo()
    

    consultar_producto_especifico(201)
    

    consultar_producto_especifico(999)
    
    
    registrar_nuevo_producto(nombre="Lap Top", precio= 1299, stock=30)
    
   
    consultar_catalogo()