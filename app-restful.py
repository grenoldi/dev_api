from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilidades import ListaHabilidades, Habilidades

app = Flask(__name__)
api = Api(app)

devs = [
    {'id': '0',
     'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']},
    {'id': '1',
     'nome': 'Galleani',
     'habilidades': ['Python', 'Django']},
    {'id': '2',
     'nome': 'Renan Galhardo',
     'habilidades': ['Python', 'Django']},
    {'id': '3',
     'nome': 'Guilherme Bob Renoldi',
     'habilidades': ['Linux', 'Python', 'Django', 'Flask', 'Angular', 'Java', 'Spring', 'Git', 'HTML', 'CSS',
                     'JavaScript', 'MySQL', 'PostgreSQL', 'Docker']},
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Id {} de desenvolvedor inexistente!'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador do serviço que tentou acessar.'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def post(self):
        pass

    def delete(self, id):
        devs.pop(id)
        return {'status': 'Sucesso!', 'mensagem': 'Registro excluido!'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return devs[posicao]


api.add_resource(Desenvolvedor, '/devs/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/devs/')
api.add_resource(ListaHabilidades, '/habilidades/')
api.add_resource(Habilidades, '/habilidades/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
