from flask import Flask
import random
    
app = Flask(__name__)

@app.route("/materia", methods=["GET"])



def verificar():
    nombre =( ['Maria', 'José', 'Amanada', 'Lino', 'Sibeia', 'Arianna', 'Pedro', 'Ana', 'Natalia'])
    # print (random.choice(nombre))

    for n in range (0,n):
        notas=[]
        nota= random(0,10)
        if nota>5:
            mensaje = "<p>Aprobado</p>"
        else:
            mensaje = "<p>Reprobado</p>"
        notas.push({random.choice(nombre),notas, mensaje})
            

   

if __name__ == "__main__":
    app.run(debug=True)