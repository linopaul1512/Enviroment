from flask import Flask

    
app = Flask(__name__)

@app.route("/lino", methods=["GET"])
def get_request():
    return "¡hellou Lino!"

if __name__ == "__main__":
    app.run(debug=True)


#http://localhost:5000/lino