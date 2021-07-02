from modalidade import Modalidade
from ranking import Ranking as r

class Corrida(Modalidade):
    def __init__(self, json_data):
        super().__init__(**json_data)
    
    def encerra(self, competicao_id, resultados):
        ranking = r.rank(resultados, maior_vlr_primeiro=False)
        if self[competicao_id].encerrada:
            raise KeyError
        self[competicao_id].encerra(ranking)