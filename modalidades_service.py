from modalidade import Modalidade
from json_service import *
from dardo import Dardo
from corrida import Corrida

class ModalidadesService:
    def __init__(self):
        json_data = read()

        corrida = Corrida(json_data['corrida'])
        dardo = Dardo(json_data['dardo'])

        self.__modalidades = {'dardo': dardo, 'corrida': corrida}

    @property
    def modalidades(self):
        return list(self.__modalidades.values())

    def add_competicao(self, modalidade, json_data):
        self.__modalidades[modalidade].append(json_data)
        self.__write()
    
    def encerra_competicao(self, modalidade, c_id, resultados):
        self.__modalidades[modalidade].encerra(c_id, resultados)
        self.__write()
    
    def __write(self):
        print(self.__modalidades)
        d = dict([(key, dict(value)) for key, value in self.__modalidades.items()])
        write(d)

    def __getitem__(self, key):
        return self.__modalidades[key]


