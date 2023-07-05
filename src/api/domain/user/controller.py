import api.domain.user.repository as Repository
import api.response as Response
import bcrypt
from api.utils import hash_pass,  verify_user, verify_login
from flask_jwt_extended import create_access_token # PARA PODER CREAR EL TOKEN
# from cloudinary.uploader import upload



def get_users():
    response = Repository.get_users()
    return Response.response_ok(response, "Todos los usuarios", 201)


def create_user(new_user):
   correct_user = verify_user(new_user)
   if correct_user.get("error") is not None:
      return correct_user
   hashed = hash_pass(new_user['password']) 
   return Repository.create_user(new_user['email'],hashed.decode())