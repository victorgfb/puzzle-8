from borda import Borda
from no import No
import copy

class arvoreBusca():

    jaAberto = []

    def __init__(self, problema, estrategia):
        self.problema = problema
        self.estrategia = estrategia
        self.borda = Borda(estrategia)
        no = No(problema, None, None, 0, 0)
        self.borda.inserir(no)

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

arvore = arvoreBusca([[ 1,  2,  3], [ 4,  7, 6], [ 8,  5,  0]], "largura")

while(1):    
    if(arvore.borda.vazia()):
        print("error")
        break

    noAtual = arvore.borda.removerPrimeiro()
    print(noAtual.profundidade)
    for i in noAtual.estado:
        print(i)

    if(arvore.testaObjetivo(noAtual.estado)):
        print("--------------")
        for i in noAtual.estado:
            print("| " + str(i) + " |")
        print("--------------")
        break
    else:
        lista = arvore.funcaoSucessora(noAtual.estado)
        listaNos = []
        for i, estado in enumerate(lista):
            no = No(estado, noAtual,i, noAtual.custoCaminho, noAtual.profundidade)
            if(not(arvore.verificaJaAberto(no))):
                listaNos.append(no)
                arvore.inseriJaAberto(no)
        arvore.borda.inserirTodos(listaNos)