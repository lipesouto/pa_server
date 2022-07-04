import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://admin:Palavra2022@palavraanimada.o2bklie.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('pa_db')
collection = db.get_collection('sessions')

dado_teste = {
    "system":"Android",
    "ajuda": [False, False, True],
    "date_session": "20:48 22 June, 2022",
    "nivel_jogado": "easy",
    "obj_name": ["Cabine", "Pirulito", "Câmera"],
    "resposta_certa": [False, False, True],
    "resposta_errada": [True, True, False],
    "tempo": [1.7150205373764038, 0.7294141054153442, 2.292156219482422],
    "total_palavras": 16,
    "total_pontos": 220
}
collection.insert_one(dado_teste)