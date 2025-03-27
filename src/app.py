from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta"


@app.route("/")
def home():
    return render_template("index.html")


# Ruta simple
@app.route("/api/data")
def get_data():
    return jsonify({"menasje": "Hola desde API Flask", "estado": "exitoso"})


# Ruta con parámetros
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola, {nombre}!. Bienvenido a Flask"


# Ruta con método POST
@app.route("/enviar", methods=["POST"])
def recibir_datos():
    datos = request.form["dato"]
    return f"Dato recibido: {datos}"


# Manejo de sesiones
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        session["usuario"] = usuario
        return redirect(url_for("perfil"))
    return render_template("login.html")


@app.route("/perfil")
def perfil():
    if "usuario" in session:
        return f"Perfil de {session['usuario']}"
    return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("home"))


@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    # curl -X GET http://127.0.0.1:5000/suma/10/2
    return jsonify({"Resultado": a + b}), 200


@app.route("/resta/<int:a>/<int:b>")
def resta(a, b):
    # curl -X GET http://127.0.0.1:5000/resta/10/2
    return jsonify({"Resultado": a - b}), 200


@app.route("/multiplicacion/<int:a>/<int:b>")
def nultiplicacion(a, b):
    # curl -X GET http://127.0.0.1:5000/multiplicacion/10/2
    return jsonify({"Resultado": a * b}), 200


@app.route("/division/<int:a>/<int:b>")
def division(a, b):
    # curl -X GET http://127.0.0.1:5000/division/10/2
    if b == 0:
        return jsonify({"error": "No se puede dividir por cero"}), 200
    return jsonify({"Resultado": float(a / b)})


if __name__ == "__main__":
    app.run(debug=True)
