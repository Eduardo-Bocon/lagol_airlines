from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://lagoldb:lagollagol@lagol0.lojkw.mongodb.net/?retryWrites=true&w=majority&appName=Lagol0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Conectado com muito sucesso!")
except Exception as e:
    print(e)