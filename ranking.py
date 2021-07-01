class Ranking:
    @staticmethod
    def rank(valores, maior_vlr_primeiro=False, reducer=lambda i: i):
        sorted_tuples = sorted(valores.items(), key=lambda k, v: reducer(v), reverse=reverse)
        return dict([(k, v) for k, v in sorted_tuples])
