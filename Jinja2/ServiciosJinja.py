from flask import Flask,request, render_template, jsonify
import random


app = Flask(__name__, template_folder= "./Templetes")

"""
@app.route("/saludo_jinja/<nombre>", methods=["GET"])
def saludo_jinja(nombre):
    return render_template("home.html.jinja", nombre=nombre)
"""


@app.route('/listar', methods=["GET"])
def lista():
    student_names = ["John", "Jane", "Bob", "Alice", "Mike", "Emma", "Oliver", "Sophia"]
    notes = [random.randint(0, 100) for _ in range(10)]
    nombre = request.args.get('nombre')
    cantidad_str = request.args.get('cantidad')
    
    if not nombre or not cantidad_str:
        return jsonify({"errores": "Invalid request"}), 400

    try:
        cantidad = int(cantidad_str)
    except ValueError:
        return jsonify({"error": "Cantidad must be an integer"}), 400
    
    students = []
    for _ in range(cantidad):
        student_name = random.choice(student_names)
        note = random.choice(notes)
        approved = "Aprobó" if note >= 60 else "No aprobó"
        students.append({"nombre": student_name, "nota": note, "aprobado": approved})

    return render_template("ListaEstudiante.html.jinja",students = students)


@app.route("/verificarMayorEdad/<listaPersonas>", methods= ['GET'])
def verificarMayorEdad(listaPersonas):

 listaPersonas=[{"nombre" : "Lino", "edad": 20}, {"nombre" : "Lino", "edad": 20}, {"nombre" : "David", "edad": 21},
                {"nombre" : "Paula", "edad": 17}, {"nombre" : "Siberia", "edad": 21}, {"nombre" : "Jesus", "edad": 21}]
 return render_template("ListaPersonas.html.jinja",listaPersonas = listaPersonas)

if __name__ == "__main__":
    app.run(debug=True)



