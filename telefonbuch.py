from flask import Flask, request, render_template

app = Flask(__name__)

Telefonbuch = {}

@app.route("/")
def index():
    return render_template("index.html", contacts=Telefonbuch)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    nummer = request.form["nummer"]
    Telefonbuch[name] = nummer
    return index()

@app.route("/delete/<name>")
def delete(name):
    if name in Telefonbuch:
        del Telefonbuch[name]
    return index()

if __name__ == "__main__":
    app.run(debug=True)
