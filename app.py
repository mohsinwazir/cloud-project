from flask import Flask, jsonify, render_template
import mysql.connector
import os

app = Flask(__name__)

# Database configuration from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "password")
DB_NAME = os.getenv("DB_NAME", "cloud_shop")

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/shop')
def products_page():
    conn = get_db_connection()
    products = []
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error fetching products: {err}")
            if conn.is_connected():
                conn.close()
    
    return render_template('products.html', products=products)

@app.route('/api/products')
def api_products():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(products)
    except mysql.connector.Error as err:
        conn.close()
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
