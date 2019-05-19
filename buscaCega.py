from arvoreBusca import arvoreBusca
from no import No
import sys

arquivo = sys.argv[1]
modo = sys.argv[2]

print(arquivo)

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

    if(arvore.testaObjetivo(noAtual.estado)):
        print("--------------")
        for i in noAtual.estado:
            print("| " + str(i) + " |")
        print("--------------")

        p = []
        for i in noAtual.acao:
            print(i, end=", ") 
        print()
        break
    else:
        lista = arvore.funcaoSucessora(noAtual.estado)
        listaNos = []
        aux = ['u','d','l','r']
        for i, estado in enumerate(lista):
            acao = noAtual.acao[:]
            acao.append(aux[i])
            no = No(estado, noAtual, acao, noAtual.custoCaminho, noAtual.profundidade)
            if(not(arvore.verificaJaAberto(no))):
                listaNos.append(no)
                arvore.inseriJaAberto(no)
        arvore.borda.inserirTodos(listaNos)
