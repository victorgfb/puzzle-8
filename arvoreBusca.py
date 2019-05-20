from borda import Borda
from no import No
import copy

class arvoreBusca():

    jaAberto = []

    def __init__(self, problema, estrategia):
        
        if(not(self.testaSolucionavel(problema))):
            print("tabuleiro invalido")
            quit()

        self.problema = problema
        self.estrategia = estrategia
        self.borda = Borda(estrategia)
        no = No(problema, None, None, 0, 0)
        self.borda.inserir(no)

    def testaSolucionavel(self, puzzle):
        last = -1
        count = 0
        for i in puzzle:
            for j in i:
                if(j != 0):
                    if j < last:
                        count +=1
                    last = j

        return (count % 2) == 0


    def testaObjetivo(self, estadoAtual):
        anterior = 0
        for x in estadoAtual:
            for y in x:
                if (y  < anterior) and (y != 0):
                    return False
                if( y != 0):
                    anterior = y
        return True

    def encontraVazio(self, estadoAtual):
        for i, x in enumerate(estadoAtual):
            for j, y in enumerate(x):
                if(y == 0):
                    return  [i,j]

    def verificaJaAberto(self, no):
        if(no.estado in self.jaAberto):
            return True

        return False


    def inseriJaAberto(self, no):
        self.jaAberto.append(no.estado)

    def funcaoSucessora(self, estadoAtual):
        i,j = self.encontraVazio(estadoAtual)

        lista = []

        if(i != 0):
            novoEstado =  copy.deepcopy(estadoAtual)
            aux  = novoEstado[i -1][j]
            novoEstado[i -1][j] = 0
            novoEstado[i][j] = aux
            lista.append(novoEstado)

        if((i +1) < len(estadoAtual)):
            novoEstado =  copy.deepcopy(estadoAtual)
            aux  = estadoAtual[i + 1][j]
            novoEstado[i + 1][j] = 0
            novoEstado[i][j] = aux
            lista.append(novoEstado)
        
        if(j != 0):
            novoEstado =  copy.deepcopy(estadoAtual)
            aux  = estadoAtual[i][j -1]
            novoEstado[i][j - 1] = 0
            novoEstado[i][j] = aux
            lista.append(novoEstado)
        
        if((j+1) < len(estadoAtual[0])):
            novoEstado =  copy.deepcopy(estadoAtual)
            aux  = estadoAtual[i][j +1]
            novoEstado[i][j + 1] = 0
            novoEstado[i][j] = aux
            lista.append(novoEstado)

        return lista