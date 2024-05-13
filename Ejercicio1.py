from flask import Flask, request

app = Flask(__name__)


@app.route("/palindromo/<palabra>", methods=["GET"])
def verificar(palabra):

    if palabra == palabra[::-1]:
        return "Es polindromo!"
    else:
        return "No es polindromo!"


if __name__ == "__main__":
    app.run(debug=True)
#http://localhost:5000/palindromo/lino lino pude ser ambiado po otra palabra