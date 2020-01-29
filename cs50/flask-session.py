from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []


@app.route("/", methods=["GRT", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        note.append(note)
    return render_template("notes.html", notes=notes)
