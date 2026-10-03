from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to tp-devsecops"

@app.route("/search")
def search():
    user = request.args.get("user", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.execute(f"SELECT * FROM users WHERE name = '{user}'")
    return str(cursor.fetchall())

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return result.decode()

if __name__ == "__main__":
    app.run(debug=True)
