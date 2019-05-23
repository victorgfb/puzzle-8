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

#Realiza leitura do quebra cabeça do  arquivo

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
    
arvore = arvoreBusca(l, modo)

if(arvore.borda.vazia()):
        print("Error: não foi possivel encontrar a solução.")
        quit()
noAtual = arvore.borda.removerPrimeiro()

while(not(arvore.testaObjetivo(noAtual.estado))):    
    print(noAtual.profundidade)

    for i in noAtual.estado:
        print(i)

    print("\n\n")

    listaNos = noAtual.funcaoSucessora()
    arvore.borda.inserirTodos(listaNos)
    if(arvore.borda.vazia()):
        print("Error: não foi possivel encontrar a solução.")
        quit()
    noAtual = arvore.borda.removerPrimeiro()

print("--------------")
print("---SOLUÇÂO---")
for i in noAtual.estado:
    print("| " + str(i) + " |")
print("--------------")

aux = copy.copy(noAtual)

#imprime sequencia de passos para resolver o quebra cabeça.

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

fim = time.time()
print("\nTempo de execução = ", fim - ini)