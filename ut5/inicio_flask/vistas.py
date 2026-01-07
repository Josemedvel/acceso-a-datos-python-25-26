from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def inicio():
    data = {}
    data["nombre"] = "Sandra"
    data["email"] = "sandra@email.com"

    return render_template("index.html", datos = data)

if __name__ == "__main__":
    app.run(debug=True)