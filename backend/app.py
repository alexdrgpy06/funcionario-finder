from flask import Flask, jsonify
from scraping.funcionarios import obtener_funcionarios
from scraping.noticias import buscar_noticias
import json
app = Flask(__name__)
@app.route('/api/funcionarios', methods='get')
def get_funcionarios():
    funcionarios = obtener_funcionarios()
    for funcionario in funcionarios:
        funcionario['noticias'] = buscar_noticias(funcionario)
    return jsonify(funcionarios)
if __name__ == '__main__':
    app.run(debug=True)
