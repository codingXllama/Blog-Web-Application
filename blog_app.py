from flask import Flask,render_template

app=Flask(__name__)

# Creating a list of dictionary,where each dictionary is a post

userPosts = [
    {
        "User": "Sam X",
        "Content": "I love this pizza, give it a try!",
        "title": "Nix Pizza Shop",
        "postDate":" May 20, 1980"
    },
    {
        "User": "Nuxa N",
        "Content": "Wow this Ice-cream is so delicious",
        "title": "Amazing Ice",
        "postDate":"October 2,1998"
    }
]



@app.route("/")
def Home():
    #sending the userposts as post
    return render_template("home.html",posts=userPosts)

#Routing to the About page
@app.route("/about")
def About():
    return render_template("about.html")


#Running the app in Debug mode

if __name__ == "__main__":
    app.run(debug=True)
