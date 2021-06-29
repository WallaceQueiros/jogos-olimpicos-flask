class Atleta:
    def __init__(self, nome, idade, altura, peso):
        self.__data = dict()
        self.__data['nome'] = nome
        self.__data['idade'] = idade
        self.__data['altura'] = altura
        self.__data['peso'] = peso

    @property
    def nome(self):
        return self.__data['nome']

    @property
    def idade(self):
        return self.__data['idade']
    
    @property
    def altura(self):
        return self.__data['altura']

    @property
    def peso(self):
        return self.__data['peso']

    def __dict__(self):
        return self.__data
