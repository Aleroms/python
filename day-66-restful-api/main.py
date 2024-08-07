import json

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# vars
SECRETE_APIKEY = 'TopSecretAPIKey'


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get_random_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars()
    random_cafe = random.choice(all_cafes)


@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search')
def search_cafe():
    query_loc = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_loc))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

    return jsonify({"error": "no such location found"})


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        has_sockets=bool(request.form.get('has_sockets')),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route('/update_price/<int:cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get('new_price')
    coffee = db.get_or_404(Cafe, cafe_id)
    if coffee:
        coffee.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "successfully updated the price"})

    return jsonify(error={"Not Found": "Cafe Item not found"})


# HTTP DELETE - Delete Record
@app.route('/report_closed/<int:cafe_id>', methods=["DELETE"])
def report_cafe_closed(cafe_id):
    req_apikey = request.args.get('apikey')

    # check api key first
    if req_apikey == SECRETE_APIKEY:
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(result={"Success": "Successfully removed cafe from database."}), 200

        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

    return jsonify(error={"Forbidden": "Sorry a cafe with that id was not found in the database"})


if __name__ == '__main__':
    app.run(debug=True)
