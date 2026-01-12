from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

@app.route("/health")
def health():
    return jsonify({"status": "OK"}), 200

@app.route("/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR, role VARCHAR);")
    cur.execute("INSERT INTO users (name, role) VALUES ('Somu', 'Associate Engineer') RETURNING id, name, role;")
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"user": result})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
