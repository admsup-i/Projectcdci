from flask import Flask, jsonify
import datetime

app = Flask(__name__)

APP_VERSION = "1.0.0"


@app.route("/")
def home():
    return jsonify({
       "message": "Hello from the CI/CD demo app! iliyas",
        "version": APP_VERSION
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }), 200


@app.route("/add/<int(signed=True):a>/<int(signed=True):b>")
def add(a, b):
    return jsonify({"a": a, "b": b, "result": a + b})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
