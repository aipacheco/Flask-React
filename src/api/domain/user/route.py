from flask import Flask, request, jsonify, url_for, Blueprint
from api.models.index import db, User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, get_jwt
import api.domain.user.controller as Controller
import api.response as Response
import json

api = Blueprint('api/user', __name__)


@api.route("/", methods= ["GET"])
def get_users():
    return Controller.get_users()

@api.route('/register', methods=['POST'])
def create_user():
        body = request.get_json()
        new_user = Controller.create_user(body)   
        if isinstance(new_user, User):   
            return Response.response_ok(new_user.serialize(), "Usuario registrado correctamente", 201)
        return new_user #para que recoja el error de la funcion validar_usuario