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

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
