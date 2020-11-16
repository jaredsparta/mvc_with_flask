from flask import Flask

# Create an instance of an app
app = Flask(__name__)

students = [
    {"id": 0, "title":"Mr.", "firstname":"Jared", "lastname":"Solano", "course":"DevOps"}
    ]

# Use the app.route decorator
# The localhost:5000 is the default port for Flask
@app.route("/")
def home():
    return "This is a dream team of DevOps consultants"

if __name__ == "__main__":
    app.run(debug=True)