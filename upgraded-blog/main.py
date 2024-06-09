from flask import Flask, render_template, request
import requests
import os

all_posts = requests.get(url="https://api.npoint.io/cc1cda32a0a4d0c4315a").json()
app = Flask(__name__)
email = os.environ["email"]
pw = os.environ["password"]


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', submitted=True)

    return render_template("contact.html", submitted=False)




@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    return f"<h1>Thank you {name}. Your message has been received</h1>"


@app.route('/post/<int:postId>')
def post(postId):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == postId:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
