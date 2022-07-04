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
    # dado_teste = {
    #     "system": request.form.get('system'),
    #     "ajuda": request.form.get('ajuda'),
    #     "date_session": request.form.get('date_session'),
    #     "nivel_jogado": request.form.get('nivel_jogado'),
    #     "obj_name": request.form.get('obj_name'),
    #     "resposta_certa": request.form.get('resposta_certa'),
    #     "resposta_errada": request.form.get('resposta_errada'),
    #     "tempo": request.form.get('tempo'),
    #     "total_palavras": request.form.get('total_palavras'),
    #     "total_pontos": request.form.get('total_pontos'),
    # }

    dado_teste = request.form('data')
    print("Data Response: ", dado_teste)
    #collection.insert_one(dado_teste)

    return "Session salva com sucesso"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
