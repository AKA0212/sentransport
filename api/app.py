import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Charger les données depuis le fichier JSON
with open("lignes_ddd.json", "r", encoding="utf-8") as f:
    lignes = json.load(f)

@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>", "/arrets", "/stats", "/lignes/recherche?q="]
    })

@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)

@app.route("/lignes/recherche")
def recherche_lignes():
    q = request.args.get("q", "").lower()

    if not q:
        return jsonify({"erreur": "Paramètre q manquant. Exemple : /lignes/recherche?q=Pikine"}), 400

    resultats = [
        ligne for ligne in lignes
        if q in ligne["depart"].lower() or q in ligne["arrivee"].lower()
    ]

    if not resultats:
        return jsonify({"message": f"Aucune ligne trouvée pour '{q}'", "resultats": []}), 404

    return jsonify({
        "query": q,
        "nombre_resultats": len(resultats),
        "resultats": resultats
    })

@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next((l for l in lignes if l["id"] == ligne_id), None)
    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvée"}), 404
    return jsonify(ligne)

@app.route("/arrets")
def get_arrets():
    arrets_set = set()
    for ligne in lignes:
        for arret in ligne["listeArrets"]:
            arrets_set.add(arret)
    return jsonify(list(arrets_set))

@app.route("/stats")
def get_stats():
    nombre_lignes = len(lignes)
    nombre_total_arrets = sum(len(ligne["listeArrets"]) for ligne in lignes)
    ligne_max = max(lignes, key=lambda l: len(l["listeArrets"]))

    return jsonify({
        "nombre_total_lignes": nombre_lignes,
        "nombre_total_arrets": nombre_total_arrets,
        "ligne_plus_darrets": {
            "id": ligne_max["id"],
            "nombre_arrets": len(ligne_max["listeArrets"])
        }
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)