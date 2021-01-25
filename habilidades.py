from flask import request
from flask_restful import Resource
import json

lista_habilidades = ['Linux', 'Python', 'Django', 'Flask', 'Angular', 'Java', 'Spring', 'Git', 'HTML', 'CSS',
                     'JavaScript', 'MySQL', 'PostgreSQL', 'Docker', 'PHP', 'Ruby']


class Habilidades(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            response = {'status': 'Erro', 'message': 'Habilidade na posicao {} nao existe.'.format(id)}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        ja_existe = lista_habilidades.count(dados['name'])
        try:
            old = lista_habilidades[id]
            if ja_existe == 0:
                lista_habilidades[id] = dados['name']
                response = {'status': 'Sucesso',
                            'message': 'Habilidade na posicao {} atualizada: {} -> {}'.format(id, old, dados['name'])}
            else:
                response = {'status': 'Erro', 'message': 'Habilidade {} ja cadastrada.'.format(dados['name'])}
        except IndexError:
            response = {'status': 'Erro', 'message': 'Habilidade na posicao {} nao existe.'.format(id)}
        return response

    def delete(self, id):
        try:
            response = {'status': 'Sucesso',
                        'message': 'Habilidade {} removida da lista.'.format(lista_habilidades[id])}
            lista_habilidades.pop(id)
        except IndexError:
            response = {'status': 'Erro', 'message': 'Habilidade na posicao {} nao existe.'.format(id)}
        return response

class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        ja_existe = lista_habilidades.count(dados['name'])
        if ja_existe == 0:
            lista_habilidades.append(dados['name'])
            return lista_habilidades[posicao]
        else:
            return {'status': 'Erro', 'message': 'Habilidade já cadastrada.'}
