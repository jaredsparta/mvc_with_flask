from flask import Flask, jsonify, redirect, url_for, render_template

# Create an instance of an app
app = Flask(__name__)

students = [
    {"id": 0, "title":"Mr.", "firstname":"Jared", "lastname":"Solano", "course":"DevOps"}
    ]

# Use the app.route decorator
# The localhost:5000 is the default port for Flask
# This function runs when the URL is "/"


# Creating our own API to display data for a specific URL
# This is the URL to navigate to in the browser for this specific view function 
# http://127.0.0.1:5000/api/v1/student/data
@app.route("/api/v1/student/data/", methods=["GET"]) 
def student_data():
    return jsonify(students)  # Using ETL: Extract Transform Load


@app.route("/welcome/")
def greet_user():
    return render_template("welcome.html")


@app.errorhandler(404)
def page_not_found(Exception):
    return redirect("/welcome/"), 404


# A dynamic way for a webpage
@app.route("/user/<username>/")
def welcome_user(username):
    return f"<h1> Welcome {username} </h1>"


@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/register/")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
