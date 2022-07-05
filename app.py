import os
from flask import Flask, request
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient(
    "mongodb+srv://admin:Palavra2022@palavraanimada.o2bklie.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('pa_db')
collection = db.get_collection('sessions')

@app.route("/", methods=["GET"])
def home():
    return "teste de inicialização"

@app.route("/saving_data_session", methods=["POST"])
def savingDataSession():
    dado_teste = {
        "system": request.json['system'],
        "ajuda": request.json['ajuda'],
        "date_session": request.json['date_session'],
        "nivel_jogado": request.json['nivel_jogado'],
        "obj_name": request.json['obj_name'],
        "resposta_certa": request.json['resposta_certa'],
        "resposta_errada": request.json['resposta_errada'],
        "tempo": request.json['tempo'],
        "total_palavras": request.json['total_palavras'],
        "total_pontos": request.json['total_pontos'],
        "version":request.json['version']
    }

    collection.insert_one(dado_teste)

    return "Session salva com sucesso"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
