import random as rd
import time
''' quick-sort'''

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


''' busca binária com análise de complexidade'''


def buscabinaria(lista,chave):
    pos_inic = 0
    pos_final = len(lista) - 1
    iteracao = 0 # quantas vezes o while vai rodar
    
    while pos_inic <= pos_final:
        pos_mid = (pos_inic + pos_final)//2 # obs // divide nosso número e pega apenas a parte inteira
        
        if chave == lista[pos_mid]:
            return print ('Posição da chave ', chave, 'na lista:', pos_mid + 1, 'e foram realizadas', iteracao + 1, 'iterações')
        if chave < lista[pos_mid]:
            pos_final = pos_mid - 1  # -1 economiza processo
        if chave > lista[pos_mid]:
            pos_inic = pos_mid + 1 # +1 economiza uma casa a ser analizada (economiza processo)
        iteracao += 1    
    return print("A chave",chave, "não se encontra na lista", 'e foram realizadas', iteracao, 'iterações')


# vamos criar uma lista com números alearórios de 0 a 100 (sem repetição)
lista100 = []
for i in range (1,101): # criamos uma lista de 100 números
    lista100.append(i)
rd.shuffle(lista100) # embaralha os elementos da nossa lista de 100 números

''' 10 elementos na lista'''
lista10 = lista100[0:10]
quicksort(lista10, 0, len(lista10)-1)
print(lista10)

inicio = time.time() # grava o tempo inicial
buscabinaria(lista10, lista10[9])
fim = time.time() # grava o tempo final
tempo_total = fim - inicio # calcula o tempo total decorrido
print(f"Tempo de execução: {tempo_total} segundos")

''' 20 elementos na lista''' # vamos selecionar os 20 primeiros elementos da lista de 100 números

lista20 = lista100[0:20] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista20,0, len(lista20)-1) # colocando-a em ordem
print(lista20)
buscabinaria(lista20, lista20[19])

'''30 elementos na lista'''

lista30 = lista100[0:30] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista30,0, len(lista30)-1) # colocando-a em ordem
print(lista30)
buscabinaria(lista30, lista30[29])

'''40 elementos na lista'''

lista40 = lista100[0:40] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista40,0, len(lista40)-1) # colocando-a em ordem
print(lista40)
buscabinaria(lista40, lista40[39])


'''50 elementos na lista'''

lista50 = lista100[0:50] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista50,0, len(lista50)-1) # colocando-a em ordem
print(lista50)
buscabinaria(lista50, lista50[49])

'''60 elementos na lista'''

lista60 = lista100[0:60] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista60,0, len(lista60)-1) # colocando-a em ordem
print(lista60)
buscabinaria(lista60, lista60[59])

'''70 elementos na lista'''

lista70 = lista100[0:70] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista70,0, len(lista70)-1) # colocando-a em ordem
print(lista70)
buscabinaria(lista70, lista70[69])

'''80 elementos na lista'''

lista80 = lista100[0:80] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista80,0, len(lista80)-1) # colocando-a em ordem
print(lista80)
buscabinaria(lista80, lista80[79])

'''90 elementos na lista'''

lista90 = lista100[0:90] # criando a list com 20 elementos ( a partir da lista 100)
quicksort(lista90,0, len(lista90)-1) # colocando-a em ordem
print(lista90)
buscabinaria(lista90, lista90[89])

'''100 elementos na lista'''

quicksort(lista100,0, len(lista100)-1) # colocando-a em ordem
print(lista100)

inicio = time.time() # grava o tempo inicial
buscabinaria(lista100, lista100[99])
fim = time.time() # grava o tempo final
tempo_total = fim - inicio # calcula o tempo total decorrido
print(f"Tempo de execução: {tempo_total} segundos")

