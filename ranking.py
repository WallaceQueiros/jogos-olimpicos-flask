class Ranking:
    @staticmethod
    def rank(valores, maior_vlr_primeiro=False, reducer=sum):
        tmp = [(k, reducer([float(i) for i in v])) for k, v in valores.items()]
        sorted_tuples = sorted(tmp, key=lambda i: i[1], reverse=maior_vlr_primeiro)
        return [key for key, _ in sorted_tuples]
