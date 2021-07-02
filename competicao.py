from atleta import Atleta

class Competicao:
    def __init__(self, id, nome, local, data, atletas, ranking=[]):
        self.__id = id
        self.__nome = nome
        self.__local = local
        self.__data = data
        self.__atletas = [Atleta(**a) for a in atletas]
        self.__ranking = ranking


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
        return len(self.ranking) == len(self.atletas)
    
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
            'ranking': self.__ranking
        }.items())

    def encerra(self, resultados):
        self.__ranking = resultados
         