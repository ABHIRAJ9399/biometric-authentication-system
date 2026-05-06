from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

DB_NAME = "evoting.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        voter_id = request.form["voter_id"]
        password = request.form["password"]

        conn = get_db()
        conn.execute(
            "INSERT INTO users (name, voter_id, password) VALUES (?,?,?)",
            (name, voter_id, password)
        )
        conn.commit()
        conn.close()
        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        voter_id = request.form["voter_id"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE voter_id=? AND password=?",
            (voter_id, password)
        ).fetchone()
        conn.close()

        if user:
            session["voter_id"] = voter_id
            return redirect("/biometric-choice")
    return render_template("login.html")

@app.route("/biometric-choice")
def biometric_choice():
    return render_template("biometric_choice.html")

@app.route("/fingerprint")
def fingerprint():
    return render_template("fingerprint.html")

@app.route("/fingerprint-verify")
def fingerprint_verify():
    voter_id = session["voter_id"]
    conn = get_db()
    conn.execute(
        "INSERT INTO biometric_status (voter_id, fingerprint) VALUES (?,?)",
        (voter_id, "VERIFIED")
    )
    conn.execute(
        "UPDATE users SET biometric_type='Fingerprint' WHERE voter_id=?",
        (voter_id,)
    )
    conn.commit()
    conn.close()
    return redirect("/vote")

@app.route("/face")
def face():
    return render_template("face.html")

@app.route("/face-verify")
def face_verify():
    voter_id = session["voter_id"]
    conn = get_db()
    conn.execute(
        "INSERT INTO biometric_status (voter_id, face) VALUES (?,?)",
        (voter_id, "VERIFIED")
    )
    conn.execute(
        "UPDATE users SET biometric_type='Face' WHERE voter_id=?",
        (voter_id,)
    )
    conn.commit()
    return redirect("/vote")
    conn.close()

@app.route("/vote", methods=["GET", "POST"])
def vote():
    voter_id = session["voter_id"]  

    conn = get_db()
    already_voted = conn.execute(
        "SELECT * FROM votes WHERE voter_id = ?",
        (voter_id,)
    ).fetchone()
    if already_voted:
        conn.close()
        return "❌ You have already voted"

    if request.method == "POST":
        party = request.form["party"]

        conn.execute(
            "INSERT INTO votes (voter_id, party) VALUES (?, ?)",
            (voter_id, party)
        )
        conn.commit()
        conn.close()

        return redirect("/success")

    conn.close()
    return render_template("vote.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)
