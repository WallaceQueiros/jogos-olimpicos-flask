class Ranking:
    def __init__(self, maior_vlr_primeiro=False, reducer=lambda i: i):
        self.__reverse = maior_vlr_primeiro
        self.__reducer = reducer

    def rank(self, valores):
        sorted_tuples = sorted(valores.items(), key=lambda k, v: self.__reducer(v), reverse=self.__reverse)
        return dict([(k, v) for k, v in sorted_tuples])
