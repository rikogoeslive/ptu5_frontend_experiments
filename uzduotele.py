from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Sukurti programą, kuri turėtų statinį puslapį, pvz. localhost:5000 su norimu tekstu (rekomenduojama naudoti šablonus)"

@app.route("/penkis_kartus")
def penkis_kartus():
    return render_template("penkis_kartus.html")

@app.route("/keliamieji")   
def keliamieji():
    return render_template("keliamieji.html")

@app.route("/atsakymas")
def atsakymas():
    e_year = int(request.args["metai"])
    if (e_year % 400 == 0) or (e_year %100 != 0 and e_year %4 ==0):
        rezultatas = "keliamieji"
    else:
        rezultatas = "Ne keliamieji"
    return render_template("atsakymas.html", **request.args, rezultas=rezultatas, e_year=e_year)

if __name__ == "__main__":
    app.run(debug=True)


  