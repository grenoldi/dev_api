from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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


@app.route('/devs/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Id {} de desenvolvedor inexistente!'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador do serviço que tentou acessar.'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'Sucesso!', 'mensagem': 'Registro excluido!'})


@app.route('/devs/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return jsonify(devs[posicao])
    elif request.method == 'GET':
        return jsonify(devs)


if __name__ == '__main__':
    app.run(debug=True)
