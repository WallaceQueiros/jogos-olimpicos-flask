from modalidade import Modalidade
from json_service import *
from ranking import Ranking

class ModalidadesService:
    def __init__(self):
        json_data = read()

        corrida = Modalidade(
            **json_data['corrida'], 
            ranking=Ranking()
        )
        
        dardo = Modalidade(
            **json_data['dardo'], 
            ranking = Ranking(maior_vlr_primeiro=True, reducer=max)
        )

        self.__modalidades = dict({'dardo': dardo, 'corrida':corrida})
    
    @property
    def data(self):
        return self.__modalidades

    def add_competicao(self, modalidade, data):
        competicao = Competicao(**data)
        self.data[modalidade].competicoes += [competicao]
        write(self.data)
    
    def list_competicao(self, modalidade):
        return self

    def __getitem__(self, key):
        return self.data[key]
        
    

        
