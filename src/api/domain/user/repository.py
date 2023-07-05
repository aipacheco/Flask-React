from api.models.index import db, User
from flask import request, jsonify
from api.utils import  hash_pass
import bcrypt
import api.response as Response
from werkzeug.security import generate_password_hash, check_password_hash


def get_users():
    users = User.query.all()
    all_users = list(map(lambda user: user.serialize(), users))
    return all_users


def create_user(email, password):
    new_user = User(email, password)
    db.session.add(new_user)
    db.session.commit()
    return new_user