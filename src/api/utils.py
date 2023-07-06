from flask import jsonify, url_for
import bcrypt

def hash_pass(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def verify_user(new_user):
    required_fields = {
        'email': "El campo email debe estar completo",
        'password': "El campo contraseña no puede estar vacío",
    }

    for field, error_msg in required_fields.items():
        if new_user[field] is None or new_user[field] == "":
            return {"msg": error_msg, "error": True, "status": 400}
        
        if field == 'password' and len(new_user[field]) < 8:
            return {"msg": "La contraseña debe tener al menos 8 caracteres", "error": True, "status": 400}
        
        if field == 'password' and len(new_user[field]) > 20 :
            return {"msg": "La contraseña debe ser como máximo de 20 caracteres", "error": True, "status": 400}

    return new_user

def verify_login(user):  
   if user['email'] is  None or user['email'] == "":
      return{ "msg" : "Datos de acceso incorrectos!", "error": True,"status": 400}
   if user['password'] is  None or user['password'] == "":
      return{ "msg" : "Datos de acceso incorrectos!", "error": True,"status": 400}
   return user

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    links = ['/admin/']
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if "/admin/" not in url:
                links.append(url)

    links_html = "".join(["<li><a href='" + y + "'>" + y + "</a></li>" for y in links])
    return """
        <div style="text-align: center;">
        
        <h1 style="margin-top: 100px">API Admin </h1>
        <p>API HOST: <script>document.write('<input style="padding: 5px; width: 300px" type="text" value="'+window.location.href+'" />');</script></p>
        <p>Remember to specify a real endpoint path like: </p>
        <ul style="text-align: left">"""+links_html+"</ul></div>"


