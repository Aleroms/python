from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
app.secret_key = 'test'


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data)
    return render_template('login.html', form=form)


def validAuth(email, password):
    if email == 'admin@email.com' and password == '12345678':
        return 'success.html'
    else:
        return 'denied.html'


if __name__ == '__main__':
    app.run(debug=True)
