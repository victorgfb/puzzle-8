from arvoreBusca import arvoreBusca
from no import No

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
