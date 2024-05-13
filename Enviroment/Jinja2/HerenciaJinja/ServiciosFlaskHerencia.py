from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/task", methods=["GET"])
def tasks(): 

    listaTareas = [
    "Afetitarme la barba cada 3 días",
    "Montar las arepas",
    "Desayunar",
    "Alistarme",
    "Ir a GracoSoft"]



    return render_template("lista.html.jinja", listaTareas = listaTareas)

@app.route("/about", methods=["GET"])
def about():
    return render_template('about_me.html.jinja')



if __name__ == "__main__":
    app.run(debug=True)



