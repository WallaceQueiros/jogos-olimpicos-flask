from competicao import Competicao
from ranking import Ranking
from abc import ABC, abstractmethod


class Modalidade(ABC):
    def __init__(self, id, titulo, competicoes, provas, image):
        self.__provas = int(provas)
        self.__image = image
        self.__id = id
        self.__titulo = titulo
        self.__competicoes = [Competicao(**c) for c in competicoes]
    
    @property
    def provas(self):
        return self.__provas

    @property
    def img(self):
        return self.__image

    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def competicoes(self):
        return self.__competicoes

    def append(self, competicao_data):
        qnt = len(self.__competicoes)
        competicao = Competicao(id=qnt, **competicao_data)
        self.competicoes.append(competicao)
        
    
    def __getitem__(self, competicao_id):
        return self.competicoes[competicao_id]
    
    def __iter__(self):
        return iter({
            'provas': self.provas,
            'image': self.img,
            'id': self.id,
            'titulo': self.titulo,
            'competicoes': [dict(c) for c in self.__competicoes],
        }.items())

    @abstractmethod
    def encerra(self, competicao_id, resultados):
        pass
