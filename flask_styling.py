from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("styling/home.html")


@app.route("/containers")
def containers():
    return render_template("styling/containers.html")

if __name__ == "__main__":
    app.run(debug=True)