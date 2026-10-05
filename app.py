import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the DevOps Practical Lab Application!"

@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/db-check')
def db_check():
    # Fetch Redis host from environment variables (defaults to localhost)
    redis_host = os.environ.get('REDIS_HOST', 'localhost')
    try:
        r = redis.Redis(host=redis_host, port=6379, socket_connect_timeout=2)
        r.ping()
        return jsonify({"status": "CONNECTED", "database": f"Redis at {redis_host}"}), 200
    except Exception as e:
        return jsonify({"status": "DISCONNECTED", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
