class No:
    def __init__(self, estado, noPai, acao, custoCaminho, profundidade):
        self.estado = estado
        self.noPai = noPai
        self.acao = acao
        self.custoCaminho = custoCaminho + 1
        self.profundidade = profundidade + 1