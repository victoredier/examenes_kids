import os
import json
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "examenes_secreto_2024"
app.jinja_env.globals.update(enumerate=enumerate)

EXAMS_DIR = os.path.join(os.path.dirname(__file__), "examenes")

def load_exam(filename):
    path = os.path.join(EXAMS_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def list_exams():
    if not os.path.exists(EXAMS_DIR):
        os.makedirs(EXAMS_DIR)
    files = [f for f in os.listdir(EXAMS_DIR) if f.endswith(".json")]
    return files

@app.route("/")
def index():
    exams = list_exams()
    return render_template("index.html", exams=exams)

@app.route("/examen/<filename>")
def examen(filename):
    try:
        data = load_exam(filename)
    except FileNotFoundError:
        return "Examen no encontrado", 404
    session["exam_file"] = filename
    session["answers"] = {}
    return render_template("examen.html", data=data, filename=filename)

@app.route("/submit", methods=["POST"])
def submit():
    filename = session.get("exam_file")
    if not filename:
        return redirect(url_for("index"))
    try:
        data = load_exam(filename)
    except FileNotFoundError:
        return redirect(url_for("index"))

    preguntas = data.get("preguntas", [])
    total = len(preguntas)
    correctas = 0
    resultados = []

    for i, pregunta in enumerate(preguntas):
        key = f"pregunta_{i}"
        respuesta_usuario = request.form.get(key, "")
        respuesta_correcta = pregunta.get("respuesta", "")
        es_correcta = respuesta_usuario.strip().lower() == respuesta_correcta.strip().lower()
        if es_correcta:
            correctas += 1
        resultados.append({
            "enunciado": pregunta.get("enunciado", ""),
            "opciones": pregunta.get("opciones", {}),
            "respuesta_correcta": respuesta_correcta,
            "respuesta_usuario": respuesta_usuario,
            "es_correcta": es_correcta,
        })

    # Calificación de 0 a 5
    calificacion = round((correctas / total) * 5, 1) if total > 0 else 0

    return render_template(
        "resultado.html",
        materia=data.get("materia", ""),
        total=total,
        correctas=correctas,
        calificacion=calificacion,
        resultados=resultados,
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
