# WEB FRAMEWORKS
# webframework is a template for building web applications. 
# It provides a structure and set of tools to simplify the development process. 
# Web frameworks handle common tasks such as routing, templating, and database interactions, 
# allowing developers to focus on writing application-specific code.

# install flask by running pip install flask in terminal

from flask import Flask

#create a flask app
app = Flask(__name__)

@app.route("/") #route decorator
def home():
    return "Hello, World!" #what to show when user visits the home page

@app.route("/user/<name>") #dynamic route
def user(name):
    return f"Hello, {name}!" #what to show when user visits the user page

#run the app
if __name__ == "__main__":
    app.run(debug=True) #run the app in debug mode