from flask import Flask, request, render_template

app = Flask(__name__)

usuarios = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        usuarios.append({"nome": nome, "email": email})
    return render_template("index.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
