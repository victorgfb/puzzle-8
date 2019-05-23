import copy

class No:
    def __init__(self, estado, noPai, acao, custoCaminho, profundidade):
        self.estado = estado
        self.noPai = noPai
        self.acao = []
        if( acao != None):
            self.acao.extend(acao)
        self.custoCaminho = custoCaminho + 1
        self.profundidade = profundidade + 1
        self.heuristica = self.manhattanDistance(estado)

    def encontraVazio(self):
        for i, x in enumerate(self.estado):
            for j, y in enumerate(x):
                if(y == 0):
                    return  [i,j]

    def funcaoSucessora(self):
        i,j = self.encontraVazio()

        lista = []

        if(i != 0):
            novoEstado =  copy.deepcopy(self.estado)
            aux  = novoEstado[i -1][j]
            novoEstado[i -1][j] = 0
            novoEstado[i][j] = aux
            lista.append([novoEstado,'c'])

        if((i +1) < len(self.estado)):
            novoEstado =  copy.deepcopy(self.estado)
            aux  = self.estado[i + 1][j]
            novoEstado[i + 1][j] = 0
            novoEstado[i][j] = aux
            lista.append([novoEstado,'b'])
        
        if(j != 0):
            novoEstado =  copy.deepcopy(self.estado)
            aux  = self.estado[i][j -1]
            novoEstado[i][j - 1] = 0
            novoEstado[i][j] = aux
            lista.append([novoEstado,'e'])
        
        if((j+1) < len(self.estado[0])):
            novoEstado =  copy.deepcopy(self.estado)
            aux  = self.estado[i][j +1]
            novoEstado[i][j + 1] = 0
            novoEstado[i][j] = aux
            lista.append([novoEstado, 'd'])

        
        return lista

    def manhattanDistance(self, estado):
        count = 0
        aux = 0
        for i, elemento in enumerate(estado):
            for j,_ in enumerate(elemento):
                aux += 1
                aux3 = aux
                if (estado[i][j] != aux) and estado[i][j]:
                    aux2 = i*3 + j
                    if(aux2 >= (estado[i][j])):
                        aux2 -= 3
                        while(aux2 >= (estado[i][j] - 1)):
                            aux2 -= 3
                            count += 1
                            aux3 -= 3
                    else:
                        aux2 +=3
                        while(aux2 <= (estado[i][j])):
                                aux2 += 3
                                count += 1
                                aux3 +=3
                
                    count +=  abs(aux3 - estado[i][j])                       
        return count
    
    def getHeuristica(self):
        return self.heuristica
        