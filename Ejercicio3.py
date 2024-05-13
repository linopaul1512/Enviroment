from flask import Flask, jsonify
import json
    
app = Flask(__name__)

@app.route("/json", methods=["GET"])
def despedir():
        adad = 21
        nombre = 'Jose'
        return jsonify({'Nombre': nombre, 'edad': adad})
if __name__ == "__main__":
    app.run(debug=True)