from ..models.competicao import Competicao
from ..ranking import Ranking

class Modalidade:
    def __init__(self, id, titulo, competicoes, ranking):
        self.__data['id'] = id
        self.__data['titulo'] = titulo
        self.__data['competicoes'] = competicoes
        self.__data['ranking'] = ranking

    @property
    def ranking(self):
        return self.__data['ranking']

    @property
    def data(self):
        return self.__data['competicoes']

    @property.setter
    def data(self, lista):
        self.__data['competicoes'] = lista

    @property
    def data(self):
        return self.__data['titulo'], self.__data['competicoes']

    def add_competicao(self, competicao_data):
        qnt = len(self.data)
        competicao = Competicao(id=qnt, **data)
        self.__data['competicoes'].append(competicao)

    def close_competicao(self, competicao_id, resultados):
        ranking = self.__data['ranking'].rank(resultados)
        self.data[competicao_id].close(ranking)

