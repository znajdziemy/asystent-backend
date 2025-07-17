from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # otwiera dostęp dla frontendu

@app.route("/api/query", methods=["POST", "GET"])
def query():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    data = request.get_json(silent=True) or {}
    query = data.get("query", "")
    result = f"Wyniki dla: {query}\n - OLX: Przykładowy wynik\n - Allegro: Przykładowy wynik\n - Ceneo: Przykład\n - AliExpress: Przykład"
    return jsonify({"result": result})

@app.route("/")
def root():
    return "Backend działa ✅", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
