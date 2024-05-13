from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
listaTareas = []
@app.route("/agregaTareas", methods=["GET", "POST"])
def agregarTarea(): 

    

    if request.method == "POST":

        name = request.form.get("name")
        description = request.form.get("description")

        if name != "jugar":
            listaTareas.append({"name" : name, "description": description})
        else:
            return jsonify({"errores": "Invalid request"}, 400)




    return render_template("Agregartareas.html.jinja", listaTareas = listaTareas)


if __name__ == "__main__":
    app.run(debug=True)




