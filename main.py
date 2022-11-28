from flask import Flask, jsonify
import pymongo
import os

app = Flask(__name__)


@app.route('/')
def index():

    try:
        cliente=pymongo.MongoClient("mongodb+srv://root:s1st3m4s@dbtemp.e6lolhj.mongodb.net/?retryWrites=true&w=majority")
        db=cliente.ecoSens
        collection=db.temp
        print("Colección iniciada")
        
        datos=list(collection.find())
        print(datos)
        for x in datos:
            print(x)
        cliente.close()
        print("Conexión cerrada")

    except pymongo.errors.ServerSelectionTimeoutError as errorTime:
        return jsonify({"Choo Choo": "error de conexion1"})
    except pymongo.errors.ConnectionFailure as errorConexion:
        return jsonify({"Choo Choo": "error de conexion2"})

    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
