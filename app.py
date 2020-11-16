from flask import Flask, jsonify

# Create an instance of an app
app = Flask(__name__)

students = [
    {"id": 0, "title":"Mr.", "firstname":"Jared", "lastname":"Solano", "course":"DevOps"}
    ]

# Use the app.route decorator
# The localhost:5000 is the default port for Flask
# This function runs when the URL is "/"
@app.route("/")
def home():
    return "<h1> This is a dream team of DevOps consultants </h1>"

# Creating our own API to display data for a specific URL
# This is the URL to navigate to in the browser for this specific view function 
# http://127.0.0.1:5000/api/v1/student/data
@app.route("/api/v1/student/data", methods=["GET"]) 
def student_data():
    return jsonify(students)  # Using ETL: Extract Transform Load


if __name__ == "__main__":
    app.run(debug=True)
