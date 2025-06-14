from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/info')
def info():
    return jsonify(status="ok", message="test info")

app.run(host='0.0.0.0', port=5000)
