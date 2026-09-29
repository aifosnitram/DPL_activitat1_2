from flask import Flask

app = Flask(__name__)

@app.route("/")
def inici():
    return """
    <h1>Desplegament d'Aplicacions Web</h1>
    <p>La meva primera aplicació desplegada amb Render.</p>
    """

@app.route("/alumne/sofia")
def alumne():
    return f"""
    <h1>Hola, Sofia!</h1>
    <p>Aquesta pàgina ha estat generada pel servidor.</p>
    """