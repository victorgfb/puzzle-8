from numpy import abs
from no import No

class Borda:

    l = []

    def __init__(self, estrategia):
        self.estrategia = estrategia

    def vazia(self):
        if len(self.l) == 0:
            return True
        else:
            return False
    
    def inserir(self, no):
        self.l.append(no)

    def verificaHeuristica(self):
        for i in self.l:
            num = self.manhattanDistance(i.estado)
            i.heuristica = num
        aux = sorted(self.l, key = No.getHeuristica)
        self.l = aux

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
    
    def removerPrimeiro(self):
        if(self.estrategia == "largura"):
            return self.l.pop(0)
        elif(self.estrategia == "profundidade"):
            return self.l.pop()
        elif (self.estrategia == "a"):
            self.verificaHeuristica()
            return self.l.pop(0)

    def inserirTodos(self, nos):
        self.l.extend(nos)

    def imprimir(self):
        for x in self.l:
            for k in x.estado:
                print(k)
            print(" ")
        