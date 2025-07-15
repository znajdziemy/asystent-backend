from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Zezwala na żądania z dowolnej domeny do endpointów /api/*
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/query", methods=["POST"])
def query():
    data = request.get_json()
    query = data.get("query", "")

    # Przykładowa symulacja wyników
    result = (
        f"Wyniki dla: {query}\n"
        f"- OLX: Przykładowy wynik OLX\n"
        f"- Allegro: Przykładowy wynik Allegro\n"
        f"- Ceneo: Przykładowy wynik Ceneo\n"
        f"- AliExpress: Przykładowy wynik AliExpress"
    )

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
