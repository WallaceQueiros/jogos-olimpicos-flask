from flask import Flask, redirect, request, render_template
from modalidades_service import ModalidadesService as ms
app = Flask(__name__)

@app.route('/')
def index():
    m = ms()
    modalidade = m['corrida']
    print(type(modalidade))
    print(modalidade.competicoes)
    return render_template('index.html', modalidade=modalidade)



if __name__ == '__main__':
    app.run(host="0.0.0.0")
