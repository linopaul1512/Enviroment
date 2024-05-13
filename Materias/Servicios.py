from flask import Flask, request, render_template, redirect, url_for, flash
from db import collection
from bson.objectid import ObjectId



app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "clave secreta"

elementsList = []

@app.route("/list", methods=["GET"])
def getList():
    elementsList = collection.find()

    return render_template('lista.html.jinja', elementsList=elementsList)

@app.route('/', methods=['GET', 'POST'])
def add_element():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        materia = request.form['materia']
        objetivo = request.form['objetivo']
        duracion = request.form['duracion']
        nota = request.form['nota']

        object = {
            'nombre': nombre,
            'apellido': apellido,
            'cedula': cedula,
            'materia': materia,
            'objetivo': objetivo,
            'duracion': duracion,
            'nota': nota
        }
        collection.insert_one(object)
        return redirect(url_for('getList'))
    return render_template("add.html.jinja")

@app.route('/<id>', methods=['GET'])
def get_element(id):
    oid = ObjectId(id)
    element = collection.find_one({'_id': oid})
    return render_template('detail.html.jinja', element = element)


@app.route('/update/<id>', methods=['GET', 'POST'])
def update_element(id):
    oid = ObjectId(id)
    element = collection.find_one({'_id': oid})
    if request.method == "POST":
        new_element = request.form
        collection.replace_one({'_id': oid}, 
                                         {'nombre': new_element['nombre'],
                                          'apellido': new_element['apellido'],
                                          'cedula': new_element['cedula'],
                                          'materia': new_element['materia'],
                                          'objetivo': new_element['objetivo'],
                                          'duracion': new_element['duracion'],
                                          'nota': new_element['nota'],
                                          })    
        return redirect(url_for('getList'))
    return render_template("update.html.jinja", element=element)



@app.route('/delete/<id>', methods=['GET'])
def delete_element(id):
    oid = ObjectId(id)
    element = collection.delete_one({'_id': oid})
    return redirect(url_for('getList'))


if __name__ == "__main__":
    app.run(debug=True)



