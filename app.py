from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "belleza_user"),
        password=os.environ.get("DB_PASSWORD", "belleza_pass"),
        database=os.environ.get("DB_NAME", "belleza_db")
    )

@app.route("/")
def index():
    return jsonify({"mensaje": "API GlowSkin - Cuidado Facial", "version": "1.0"})

@app.route("/productos", methods=["GET"])
def get_productos():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/productos", methods=["POST"])
def crear_producto():
    data = request.get_json()
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, precio, categoria) VALUES (%s, %s, %s, %s)",
            (data["nombre"], data["descripcion"], data["precio"], data["categoria"])
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Producto creado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/productos/<int:id>", methods=["GET"])
def get_producto(id):
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        if producto:
            return jsonify(producto)
        return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/salud", methods=["GET"])
def health():
    return jsonify({"estado": "activo"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
