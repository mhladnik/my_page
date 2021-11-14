from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    age = 27
    return render_template("about.html", age=age)

@app.route("/boogle")
def boogle():
    return render_template("/Boogle/boogle.html")

@app.route("/cvetlicarna")
def cvetlicarna():
    return render_template("/Cvetlicarna/cvetlicarna.html")

@app.route("/beautysalon")
def beautysalon():
    return render_template("/beautysalon/beautysalon.html")

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)