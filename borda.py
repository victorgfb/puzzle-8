
from numpy import abs
from no import No

class Borda:

    l = []
    jaAberto = []

    def __init__(self, estrategia):
        self.estrategia = estrategia

    def vazia(self):
        if len(self.l) == 0:
            return True
        else:
            return False
    
    def inserir(self, no):
        if(not(self.verificaJaAberto(no))):
            if(self.estrategia == "profundidade"):
                self.l.insert(0,no)
            else:
                self.l.append(no)

    def verificaHeuristica(self):
        aux = sorted(self.l, key = No.getHeuristica)
        self.l = aux
  
    def removerPrimeiro(self):
        if (self.estrategia == "gulosa"):
            self.verificaHeuristica()
        return self.l.pop(0)

    def inserirTodos(self, nos):
        for no in nos:
            self.inserir(no)

    def imprimir(self):
        for x in self.l:
            for k in x.estado:
                print(k)
            print(" ")
    
    def verificaJaAberto(self, no):
        if(no.estado in self.jaAberto):
            return True

        self.inseriJaAberto(no)
        return False

    def inseriJaAberto(self, no):
        self.jaAberto.append(no.estado)