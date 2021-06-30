from flask import Flask, redirect, request, render_template
from modalidades_service import ModalidadesService as ms
app = Flask(__name__)

@app.route('/')
def index():
    m = ms()
    return render_template('index.html', modalidades=m)

@app.route('/<modalidade>')
def competicoes(modalidade):
    m = ms()[modalidade]
    return render_template('competicoes.html', modalidade=m, competicoes=m.competicoes)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
