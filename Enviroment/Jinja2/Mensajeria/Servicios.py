from flask import Flask, request, render_template, jsonify, flash, url_for, redirect

app = Flask(__name__)


app = Flask(__name__, template_folder="./Templates")
app.config['SECRET_KEY'] = 'clave secreta'

messageList = []

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        
        content = request.form["content"]
        title = request.form["title"]

        if not title:
            flash("El título es obligatorio")
        if not content:
            flash("El título es obligatorio")

        if title and content:
            messageList.append({'title': title , 'content': content})
            return redirect(url_for('messages'))
    return render_template('contact.html.jinja')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about_me.html.jinja')

@app.route("/messages")
def messages():
    return render_template('messages.html.jinja', messages=messageList)


if __name__ == "__main__":
    app.run(debug=True)



