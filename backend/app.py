from flask import Flask, jsonify from scraping.funcionarios import obtener_funcionarios, buscar_noticias

app = Flask(__name__)

@app.route('/api/funcionarios', methods=['GET'])
def get_funcionarios():
    funcionarios = obtener_funcionarios()
    for funcionario in funcionarios:
        funcionario['noticias'] = buscar_noticias(funcionario)
    return jsonify(num=1})

if __name__ == '__main__':
    app.run(debug=True)
