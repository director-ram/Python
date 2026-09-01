from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #route decorator
def home():
    return render_template("index.html",name="Hemasai") #render the home.html template

@app.route("/user/<username>")
def user(username):
    return render_template("index.html", name=username)

if __name__ == "__main__":
    app.run(debug=True)