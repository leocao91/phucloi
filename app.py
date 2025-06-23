from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    selected = None
    if request.method == "POST":
        selected = request.form.get("benefit")
    return render_template("index.html", selected=selected)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
