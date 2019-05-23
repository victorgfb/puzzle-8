from arvoreBusca import arvoreBusca
from no import No
import time
import sys
import copy

ini = time.time()
arquivo = sys.argv[1]
modo = sys.argv[2]

if(modo != "largura") and (modo != "profundidade") and (modo != "gulosa"):
    print("modo invalido")
    quit()

f = open(arquivo, 'r')
c = f.readline()
l = []

while(len(c) > 0):
    c = c.split()
    if(len(c) != 3):
        print("entrada invalida")
        quit()
    x = [int(c[0]),int(c[1]), int(c[2])]
    c = f.readline()
    l.append(x)

if(len(l) != 3):
    print("entrada invalida")
    quit()
    

for i in l:
    print(i)

arvore = arvoreBusca(l, modo)

while(1):    
    if(arvore.borda.vazia()):
        print("error")
        break

    noAtual = arvore.borda.removerPrimeiro()
    print(noAtual.profundidade)
    for i in noAtual.estado:
        print(i)

    print("\n\n")

    if(arvore.testaObjetivo(noAtual.estado)):
        print("--------------")
        print("---SOLUÇÂO---")
        for i in noAtual.estado:
            print("| " + str(i) + " |")
        print("--------------")

        aux = copy.copy(noAtual)

        while(aux != None):
            for i in aux.estado:
                print(i)
            aux = copy.copy(aux.noPai)
            print()
        
        print("\nAções:")
        p = []
        for i in noAtual.acao:
            print(i, end=", ") 
        print("\n")

        print("Custo = ", noAtual.custoCaminho)
        break
    else:
        lista = noAtual.funcaoSucessora()
        listaNos = []

        for i, estado in enumerate(lista):
            acao = noAtual.acao[:]
            acao.append(estado[1])
            no = No(estado[0], noAtual, acao, noAtual.custoCaminho, noAtual.profundidade)
            if(not(arvore.verificaJaAberto(no))):
                listaNos.append(no)
                arvore.inseriJaAberto(no)
        arvore.borda.inserirTodos(listaNos)
fim = time.time()
print("\nTempo de execução = ", fim - ini)