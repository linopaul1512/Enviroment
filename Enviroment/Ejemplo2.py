from flask import Flask

    
app = Flask(__name__)

@app.route("/saludar/<name>", methods=["GET"])
def saludar(name):
    return f"Hola, {name}"

if __name__ == "__main__":
    app.run(debug=True)

#http://localhost:5000/saludar/lino