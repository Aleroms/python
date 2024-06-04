from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year=current_year)


@app.route('/guess/<query>')
def guess(query):
    agify_response = requests.get(url=f"https://api.agify.io?name={query}")
    agify_response.raise_for_status()
    data = agify_response.json()
    username = data["name"]
    age = data["age"]

    genderize_response = requests.get(url=f"https://api.genderize.io?name={query}")
    genderize_response.raise_for_status()
    gender = genderize_response.json()["gender"]

    return render_template('guess.html', age=age, name=username, gender=gender)


@app.route('/blog/<number>')
def get_blog(number):
    print(number)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
