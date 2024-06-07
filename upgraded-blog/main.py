from flask import Flask, render_template
import requests

all_posts = requests.get(url="https://api.npoint.io/cc1cda32a0a4d0c4315a").json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:postId>')
def post(postId):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == postId:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
