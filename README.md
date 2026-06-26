# Mi API con Flask
API mínima creada en clase para practicar Flask, Postman, requests y Git/GitHub

# Instalación
python -m venv .venv .venv\Scripts\Activate.ps1 python -m pip install -r requirements.txt

# Ejecutar servidor
python app.py

# Probar endpoints
GET http://127.0.0.1:5000/productos  
GET http://127.0.0.1:5000/productos/201
POST http://127.0.0.1:5000/productos  

## Consumir desde Python
python cliente.py
git add README.md
git commit -m "docs: agregar intrucciones de ejecucion"