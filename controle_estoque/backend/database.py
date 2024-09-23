import json

class Database:
    def __init__(self, filename='data/estoque.json'):
        self.filename = filename
        self.load()

    def load(self):
        with open(self.filename, 'r') as f:
            self.data = json.load(f)

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_produto(self, nome, quantidade, preco):
        self.data['produtos'].append({
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
        })
        self.save()

    def listar_produtos(self):
        return self.data['produtos']

    def vender_produto(self, nome, quantidade):
        for produto in self.data['produtos']:
            if produto['nome'] == nome:
                if produto['quantidade'] >= quantidade:
                    produto['quantidade'] -= quantidade
                    self.save()
                    return True
                else:
                    return False
        return False
