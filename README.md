# 🎓 Exámenes para Niños

Aplicación web creada con **Python + Flask** para realizarle exámenes a mis hijos. Permite cargar preguntas desde archivos JSON, mostrarlas de forma interactiva y calcular la calificación al finalizar.

---

## ✨ Características

- 📂 Carga exámenes automáticamente desde la carpeta `examenes/`
- 🧠 Soporta preguntas de selección múltiple (a, b, c, …)
- ✅ Valida que todas las preguntas estén respondidas antes de enviar
- 📊 Muestra la calificación del **0 al 5** al terminar
- 🔍 Revisión detallada pregunta por pregunta con respuestas correctas e incorrectas
- 📱 Diseño **responsive** — funciona bien en celular y computadora

---

## 🗂️ Estructura del proyecto

```
examenes/
├── app.py                  # Aplicación principal Flask
├── requirements.txt        # Dependencias
├── examenes/               # Carpeta con los archivos JSON de los exámenes
│   └── ciencias.json       # Ejemplo de examen
└── templates/
    ├── index.html          # Página de inicio (lista de exámenes)
    ├── examen.html         # Página de preguntas
    └── resultado.html      # Página de resultados
```

---

## 🚀 Cómo ejecutar

### 1. Instalar dependencias

```bash
pip3 install -r requirements.txt
```

### 2. Iniciar el servidor

```bash
python3 app.py
```

### 3. Abrir en el navegador

```
http://localhost:5050
```

---

## 📝 Formato del JSON de examen

Los archivos de examen deben colocarse en la carpeta `examenes/` con extensión `.json` y el siguiente formato:

```json
{
  "materia": "Ciencias",
  "preguntas": [
    {
      "enunciado": "¿Cuál es el planeta más cercano al Sol?",
      "opciones": {
        "a": "Venus",
        "b": "Mercurio",
        "c": "Marte"
      },
      "respuesta": "b"
    }
  ]
}
```

---

## 🏆 Escala de calificación

| Calificación | Significado              |
|:---:|:---|
| 5.0 | Todas las respuestas correctas |
| 3.0 | Mitad correctas               |
| 0.0 | Todas incorrectas             |

La calificación se calcula proporcionalmente: `(correctas / total) × 5`
