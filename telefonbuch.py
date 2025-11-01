from flask import Flask, request, render_template

app = Flask(__name__)

Telefonbuch = {}

@app.route("/")
def index():
    return render_template("index.html", contacts=Telefonbuch)

@app.route("/add", methods=["POST"])
def add():
    essen = request.form["essen"]
    anzahl = request.form["anzahl"]
    Telefonbuch[essen] = anzahl
    return index()

@app.route("/delete/<name>")
def delete(essen):
    if name in Telefonbuch:
        del Telefonbuch[essen]
    return index()

if __name__ == "__main__":
    app.run(debug=True)
