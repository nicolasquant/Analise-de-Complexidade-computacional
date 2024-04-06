import time
import random as rd
import matplotlib.pyplot as plt
import numpy as np


def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)
        
def partition(arr, left, right):
    i = left
    j = right -1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        
        while j > left and arr[j] >= pivot:
            j -= 1
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

''' -----------------------------------------------------'''


''' Análise de complexidade'''


def buscaSequencial(lista, chave): 
    iteracoes = 2 # 1 iteração é a quantidade de vezes que executamos cada linha de comando (não estamos contando a execução da variavel 'iteracao')
    # começamos com 2 iterações pra quebrar o laço for, ele deve ser rodado n+1 vezes. Além diso, já estamos consideradno o return.
    indice = 0
    iteracoes += 1
    for número in lista: # número in lista converte cada elemento da matriz para um número (nesse caso já é)
        iteracoes += 1
        if número == chave: # se o número achado é igual à chave, então achamos-o
            iteracoes += 1 # temos que colocar essa iteração antes do return pois o return quebra o if (como um break)
            return print("Posição da chave", chave, "na lista:", indice + 1, 'e foram realizadas', iteracoes + 1, 'iterações') # x+1 buscas pois o print do número achado está sendo executado antes do comando de aumentar x
        iteracoes += 1
        indice = indice + 1
        iteracoes += 1
        
    return print("A chave", chave, "não se encontra na lista", 'e foram realizadas', iteracoes , 'iterações')
           



'''vamos criar uma lista com números alearórios de 0 a 100 (sem repetição)'''

lista100 = []
for i in range (1,101): # criamos uma lista de 100 números
    lista100.append(i)
rd.shuffle(lista100) # embaralha os elementos da nossa lista de 100 números

''' 10 elementos na lista'''

print('LISTA COM 10 ELEMENTOS - PIOR CASO')
lista10 = lista100[0:10]
quicksort(lista10, 0, len(lista10)-1)
print(lista10)

inicio = time.time() # grava o tempo inicial
buscaSequencial(lista10, lista10[9]) # lembremos que o pior caso a ser tratado na busca sequencial ocorre quando o número a ser achado é o último
fim = time.time() # grava o tempo final
tempo_total = fim - inicio # calcula o tempo total decorrido
print(f"Tempo de execução: {tempo_total} segundos \n")


'''50 elementos na lista'''

print('LISTA COM 50 ELEMENTOS - PIOR CASO')
lista50 = lista100[0:50] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista50,0, len(lista50)-1) # colocando-a em ordem
print(lista50)

inicio = time.time() # grava o tempo inicial
buscaSequencial(lista50, lista50[49])
fim = time.time() # grava o tempo final
tempo_total = fim - inicio # calcula o tempo total decorrido
print(f"Tempo de execução: {tempo_total} segundos \n")

'''100 elementos na lista'''

print('LISTA COM 100 ELEMENTOS - PIOR CASO')
quicksort(lista100,0, len(lista100)-1) # colocando-a em ordem
print(lista100)

inicio = time.time() # grava o tempo inicial
buscaSequencial(lista100, lista100[99])
fim = time.time() # grava o tempo final
tempo_total = fim - inicio # calcula o tempo total decorrido
print(f"Tempo de execução: {tempo_total} segundos")

''' plotando o gráfico de iterações em função do tamanho da nossa array'''

xpoints = np.array([33,152,303])
ypoints = np.array([10,50,100])
plt.xlabel('número de iterações')
plt.ylabel("Tamanho da nossa matriz")
plt.title('Análise de complexidade da busca sequencial - pior caso (3n + 3)')
plt.plot(xpoints, ypoints, 'o:b') 
plt.show()

