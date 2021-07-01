from flask import Flask, redirect, request, render_template, Response, url_for
from modalidades_service import ModalidadesService
app = Flask(__name__)

@app.route('/')
def index():
    lista_modalidades = ModalidadesService()
    print(lista_modalidades.modalidades)
    return render_template('index.html', modalidades=lista_modalidades.modalidades)

@app.route('/<modalidade>')
def list_competicoes_controller(modalidade):
    if modalidade == 'favicon.ico':
        return url_for('static', filename=modalidade)
    modalidade = ModalidadesService()[modalidade]
    return render_template('competicoes.html', modalidade=modalidade, competicoes=modalidade.competicoes)

@app.route('/<modalidade>/cadastro/', methods=['POST', 'GET'])
def competicoes_cadastro_controller(modalidade):
    modalidades = ModalidadesService()
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(data)
        modalidades.add_competicao(modalidade, data)
        return redirect(f'/{modalidade}/')
    return render_template('competicoes_cadastro.html', modalidade=modalidades[modalidade])

@app.route('/<modalidade>/cadastro/resultados', methods=['POST'])
def create_resultados_controller(modalidade):
    data = request.get_json(force=True)
    modalidades = ModalidadesService()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
