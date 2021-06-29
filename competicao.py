from .atleta import Atleta

class Competicao:
    def __init__(self, id, nome, local, data, hora, atletas, ranking=None):
        self.__dados = dict()
        self.__id = id
        self.__dados['nome'] = nome
        self.__dados['local'] = local
        self.__dados['data'] = f'{data} {hora}'
        self.__dados['atletas'] = atletas
        self.__closed = False
        if ranking is not None:
            self.close(ranking)

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__dados['nome']
    
    @property
    def local(self):
        return self.__dados['local']
    
    @property
    def date(self):
        return self.__dados['data']
    
    @property
    def atletas(self):
        return [Atleta(**a) for a in self.__dados['atletas']]

    @property
    def atletas_nomes(self):
        return [a['nome'] for a in self.__dados['atletas'].items()]
    
    @property
    def data(self):
        return self.__dados

    def __dict__(self):
        return self.data

    def close(self, resultados):
        self.__dados['ranking'] = resultados
        self.__closed = True
 

        