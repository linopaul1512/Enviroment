from flask import Flask, request

#Así se corre en la web: http://localhost:5000/mensaje
app = Flask(__name__)

@app.route("/mensaje", methods=["GET", "POST"])
def message():

    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return '''
        <h1>The name value is: {}</h1>
        <h1>The message value is: {}</h1>
        '''.format(name, message)
    
    
    return  '''
            <form method="POST">
            <div><label>Name: <input type="text" name="name"></label></div>
            <div><label>Message: <input type="text" name="message"></label></div>
            <input type= "submit" value="Submit">
            </form>
            '''
    #f"Hola{name} tu mensajees: {message}""  

if __name__ == "__main__":
    app.run(debug=True)
