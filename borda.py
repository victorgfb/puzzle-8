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
    
    def removerPrimeiro(self):
        if(self.estrategia == "largura"):
            return self.l.pop(0)

    def inserirTodos(self, nos):
        self.l.extend(nos)

    def imprimir(self):
        for x in self.l:
            for k in x.estado:
                print(k)
            print(" ")
        