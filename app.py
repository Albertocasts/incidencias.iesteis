from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/incidencias", methods=["POST"])
def crear_incidencia():
    aula=request.form["Aula"]
    usuario=request.form["Usuario"]
    descripcion=request.form["Descripcion"]

    print("Aula:" + aula)
    print("Usuario:" + usuario)
    print("Descripcion:" + descripcion)
    return "Incidencia recibida"

if __name__ == "__main__":
    app.run(debug=True)
