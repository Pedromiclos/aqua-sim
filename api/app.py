from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/simulacao")
def simulacao():
    return render_template("simulacao.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    pessoas = int(request.form["pessoas"])
    area = int(request.form["area"])
    banhos = int(request.form["banhos"])

    consumo = pessoas * 3500 + area * 20 + banhos * 900
    por_pessoa = consumo / pessoas
    economia = consumo * 0.22

    return render_template(
        "resultado.html",
        consumo=round(consumo),
        por_pessoa=round(por_pessoa),
        economia=round(economia)
    )


handler = app