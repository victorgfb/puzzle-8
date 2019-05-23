from borda import Borda
from no import No
import copy

class arvoreBusca():

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
        count = 0
        aux = []

        for elemento in puzzle:
            aux.extend(elemento)

        for i, elemento in enumerate(aux):
            for proximo in aux[i:]:
                if elemento > proximo and proximo and elemento:
                    count += 1
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
