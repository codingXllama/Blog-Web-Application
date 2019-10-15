from flask import Flask

app=Flask(__name__)


@app.route("/")
def Home():
    return "<h1>Welcome to the Home Page</h1>"

#Routing to the About page
@app.route("/about")
def About():
    return "Welcome to the About Page"


#Running the app in Debug mode

if __name__ == "__main__":
    app.run(debug=True)
