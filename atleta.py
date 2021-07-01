class Atleta:
    def __init__(self, nome, idade, altura, peso):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade
    
    @property
    def altura(self):
        return self.__altura

    @property
    def peso(self):
        return self.__peso

    def __iter__(self):
        return iter({
            'nome': self.__nome,
            'idade': self.__idade,
            'altura': self.__altura,
            'peso': self.__peso
        }.items())
