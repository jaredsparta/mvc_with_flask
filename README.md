# MVC with Flask
- MVC = "Model View Controller"


- Display data on a web browser using HTML, CSS, JavaScript and Bootstrap

**Building our API**
- Display data from Flask to a specific API call/URL/endpoint

**Why Flask for our framework?**
- Flask is a mini web app frame work but very powerful
- Allows us to interact with a DB
- It can be used to create an API
- Allows us to integrate with HTMl, CSS and JS
- Allows us to map HTTP requests to Python e.g. URL and HTTP GET
- Allows us to set the API path as URL to view in the browser

<br>

# Example
- Install Flask to Python environment using `pip install Flask`
- To run the flask app: `flask run`
- We need to create an app instance: `app = Flask(__name__)`
- To create a page we need to use the `@app.route("<URL>")`:
```python
    @app.route("/welcome/")
    def greet_user():
        return "<h1> Welcome to DevOps! </h1>"
```
- Now if we go into our browser and navigate to the URL `http://127.0.0.1:5000/welcome/` we will see that. The web browser sends a request to the server which is then sent to the Flask app instance. The URL is associated with this function and this code returns the request.
- The following code redirects any `404` requests to the welcome page above:
```python
    @app.errorhandler(404)
    def page_not_found(Exception):
        return redirect("/welcome/"), 404
```

- The following page is a dynamic way to view webpages. Depending on the URL `user/<username>` it will return a different name in the greeting.
```python
    # A dynamic way for a webpage
    @app.route("/user/<username>/")
    def welcome_user(username):
        return f"<h1> Welcome {username} </h1>"
```

- Finally we run the app using the following:
```python
    if __name__ == "__main__":
        app.run(debug=True)
```

**HTML**
- Naming conventions are essential
- To use HTML templates, we need to create a `templates` folder in our directory
- Flask looks for this specific folder and anything inside it
- We will create an `index.html` file inside our templates folder