from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the DevOps Practical Lab Application!"

@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/info')
def info():
    return "App Version 1.0.0"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
