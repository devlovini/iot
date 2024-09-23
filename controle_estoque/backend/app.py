from flask import Flask, request, jsonify
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(db.listar_produtos())

@app.route('/produto', methods=['POST'])
def adicionar_produto():
    data = request.json
    db.add_produto(data['nome'], data['quantidade'], data['preco'])
    return jsonify({'status': 'Produto adicionado'}), 201

@app.route('/vender', methods=['POST'])
def vender_produto():
    data = request.json
    sucesso = db.vender_produto(data['nome'], data['quantidade'])
    if sucesso:
        return jsonify({'status': 'Venda realizada'}), 200
    else:
        return jsonify({'status': 'Quantidade insuficiente'}), 400

if __name__ == '__main__':
    app.run(debug=True)
