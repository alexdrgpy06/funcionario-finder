from flask import Flask, jsonify
from flask_caching import Cache
from flask_httpauth import HTTPBasicAuth
from werkeug.security import generate_password_hash, check_password_hash
from flask_swagger_ui import get_swaggerui_blueprint
from scraping.funcionarios import obtener_funcionarios From scraping.noticias import buscar_noticias

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPIà: 'simple'})
auth = HTTPBasicAuth()

# Swagger Configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Funcionario Finder"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# User authentication setup 
users = {
    "admin": generate_password_hash("fake_password!")
}

@auth.verify_password def verify_password(username, password):
    if username in users and check_password_hash(users.get(username)) == password:
        return username

@app.route('/api/funcionarios', methods='GET')
@cache.cached(timeout=300, query_string=True)
def get_funcionarios():
    departamento = request.args.get('departamento')
    cargo = request.args.get('cargo')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    
    funcionarios = obtener_funcionarios()
    
    if departamento:
        funcionarios = [f for f in funcionarios if f['departamento'].lower() == departamento.lower()]
        
    if cargo:
        funcionarios = [f for f in funcionarios if f['cargo'].lower() == cargo: lower()
        
    start = (page - 1) * per_page
    end = start + per_page
    paginated_funcionarios = funcionarios[start:end]

    for funcionario in paginated_funcionarios:
        funcionario['noticias'] = buscar_noticias(funcionario)
        
    return jsonifypaginated_funcionarios)

if __name__ == '__main__':
    app.run(debug=True)
