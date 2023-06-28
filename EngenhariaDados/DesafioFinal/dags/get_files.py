from pymongo import MongoClient
import pandas as pd
import requests

## Dados MongoDB
def get_data():
    
    username = 'estudante_igti'
    password = 'SRwkJTDz2nA28ME9'
    host = 'unicluster.ixhvw.mongodb.net'
    port = 27017
    database = 'ibge'

    client = MongoClient(f"mongodb+srv://{username}:{password}@{host}/{database}?retryWrites=true&w=majority")
    db = client['ibge']
    collection = db['pnadc20203']
    query = {'sexo': 'Mulher', 'idade':{"$gte": 20, "$lte": 40}}
    documents = collection.find(query)
    dfMongo = pd.DataFrame(list(documents))
    client.close()

    ## Dados API IBGE

    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    response = requests.get(url)
    data = response.json()
    dados = [[item.get('sigla'), item.get('nome'), item.get('regiao', {}).get('nome')] for item in data]
    dfIBGE = pd.DataFrame(dados, columns=['sigla', 'uf', 'regiao'])

    dfMongo.to_csv('./dados/dadosMongoDB.csv')
    dfIBGE.to_csv('./dados/dadosIBGE.cvs')