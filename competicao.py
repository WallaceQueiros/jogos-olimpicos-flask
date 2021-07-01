from atleta import Atleta

class Competicao:
    def __init__(self, id, nome, local, data, atletas, encerrada=False, ranking=None):
        self.__id = id
        self.__nome = nome
        self.__local = local
        self.__data = data
        self.__atletas = [Atleta(**a) for a in atletas]
        self.__encerrada = bool(encerrada)
        self.__ranking = ranking
        if not self.encerrada and ranking is not None:
            self.encerra(ranking)


    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
    
    @property
    def local(self):
        return self.__local
    
    @property
    def data(self):
        return self.__data
    
    @property
    def atletas(self):
        return self.__atletas

    @property
    def encerrada(self):
        return self.__encerrada
    
    @property 
    def ranking(self):
        return self.__ranking    

    @property
    def atletas_nomes(self):
        return [a.nome for a in self.atletas]

    def __iter__(self):
        return iter({
            'nome': self.nome,
            'id': self.id, 
            'local': self.local, 
            'data': self.data, 
            'atletas': [dict(a) for a in self.atletas],
            'encerrada': 1 if self.encerrada else 0,
            'ranking': self.__ranking if self.__ranking else 0
        }.items())

    def encerra(self, resultados):
        self.__ranking = resultados
        self.__encerrada = True
         