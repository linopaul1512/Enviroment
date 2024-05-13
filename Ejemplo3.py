from flask import Flask, request

    
app = Flask(__name__)

@app.route("/despedir", methods=["GET"])
def despedir():
    name = request.args.get("name")
    return f"¡Adiós, {name}"

if __name__ == "__main__":
    app.run(debug=True)

#http://localhost:5000/saludar/lino