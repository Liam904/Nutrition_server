from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    create_refresh_token,
    get_jwt,
)

from app import bcrypt
from .models import User, db


auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["POST"])
def signup():
    body = request.get_json()
    name = body.get("name")
    email = body.get("email")
    password = body.get("password")

    password = str(password)
    if not email or not name or not password:
        return jsonify({"Message": "Missing required fields"}), 400

    if len(name) < 4:
        return jsonify({"msg": "Name too short"}), 400

    if len(password) < 5:
        return jsonify({"message": "Password too short"})

    if len(email) < 5:
        return jsonify({"message": "email too short"})
    hashed_password = bcrypt.generate_password_hash(password).decode("utf8")

    new_user = User(name=name, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"Message": "Success"}), 201


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    password = str(password)

    if not email or not password:
        return jsonify({"msg": "Missing required fields"}), 400

    if not email or not password:
        return jsonify({"msg": "Missing required fields"}), 400

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return (
            jsonify({"access_token": access_token, "refresh_token": refresh_token}),
            200,
        )

    return jsonify({"msg": "Invalid email or password"}), 401
