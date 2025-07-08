from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/query", methods=["POST"])
def query():
    data = request.get_json()
    query = data.get("query", "")
    result = f"Wyniki dla: {query}\n - OLX: Przykładowy wynik\n - Allegro: Przykładowy wynik\n - Ceneo: Przykład\n - AliExpress: Przykład"
    return jsonify({"result": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
