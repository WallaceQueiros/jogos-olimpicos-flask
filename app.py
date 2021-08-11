from flask import Flask, redirect, request, render_template, Response, url_for, send_from_directory
import os
from modalidades_service import ModalidadesService
app = Flask(__name__)


@app.route('/')
def index():
    lista_modalidades = ModalidadesService()
    print(lista_modalidades.modalidades)
    return render_template('index.html', modalidades=lista_modalidades.modalidades)

@app.route('/<modalidade>')
def lista_competicoes_controller(modalidade):
    if modalidade == 'favicon.ico':
        return url_for('static', filename=modalidade)
    modalidade = ModalidadesService()[modalidade]
    return render_template('competicoes.html', modalidade=modalidade, competicoes=modalidade.competicoes)

@app.route('/<modalidade>/cadastro/', methods=['POST', 'GET'])
def cadastra_competicoes_controller(modalidade):
    modalidades = ModalidadesService()
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
        except Exception as e:
            Response('Bad Request', 400)
        modalidades.add_competicao(modalidade, data)
        return redirect(f'/{modalidade}/')
    return render_template('competicoes_cadastro.html', modalidade=modalidades[modalidade])

@app.route('/<modalidade>/<int:cid>', methods=['GET', 'POST'])
def cadastra_resultados_controller(modalidade, cid):
    modalidades = ModalidadesService()
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
        except Exception as e:
            Response('Bad Request', 400)
        print(f'data ===>{data}')
        data = dict(data)
        print(data)
        modalidades.encerra_competicao(modalidade, cid, data)
    m = modalidades[modalidade]
    competicao = m[cid]
    if competicao.encerrada:
        return render_template('resultados.html', modalidade=m, competicao=m[cid])
    return render_template('resultados_cadastro.html', modalidade=m,competicao=m[cid])

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')   

if __name__ == '__main__':
    app.run(host="0.0.0.0")
