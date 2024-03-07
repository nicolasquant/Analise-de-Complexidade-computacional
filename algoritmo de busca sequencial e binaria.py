''' Antes de qualquer coisa vamos fazer o quick_sort'''

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


''' Busca Sequencial - (n+1)/2 = número de tentativas
• A busca sequencial é o algoritmo mais simples de busca:
• Percorra a lista comparando a chave com os valores dos
elementos em cada uma das posições.
• Se a chave for igual a algum dos elementos, retorne a posição
correspondente na lista.
• Se a lista toda foi percorrida e a chave não for encontrada, retorne
o valor −1'''


def buscaSequencial(lista, chave): 
    indice = 0
    for número in lista: # número in lista converte cada elemento da matriz para um número (nesse caso já é)
        if número == chave: # se o número achado é igual à chave, então achamos-o
            return indice
        indice = indice + 1
    return -1

chave = 24
lista = [20, 5, 15, 24, 67, 45, 1, 76, 21, 11] # se a lista não estiver ordenada, use o quick_sort
quicksort(lista, 0, len(lista) - 1)
print(lista)
pos = buscaSequencial(lista, chave)

if pos != -1:
    print("Posição da chave", chave, "na lista:", pos)
else:
    print("A chave", chave, "não se encontra na lista")
# Posição da chave 45 na lista: 5


'''------------------------------------------------------------------'''

''' Busca binária - log2(n) - 1 = número de tentativas
A busca binária é um algoritmo mais eficiente, entretanto,
requer que a lista esteja ordenada pelos valores da chave de
busca.
• A ideia do algoritmo é a seguinte (assuma que a lista está
ordenada pelos valores da chave de busca):
• Verifique se a chave de busca é igual ao valor da posição do meio
da lista.
• Caso seja igual, devolva esta posição.
• Caso o valor desta posição seja maior que a chave, então repita o
processo, mas considere uma lista reduzida, com os elementos do
começo da lista até a posição anterior a do meio.
• Caso o valor desta posição seja menor que chave, então repita o
processo, mas considere uma lista reduzida, com os elementos da
posição seguinte a do meio até o final da lista. '''


lista = [1, 5, 10, 13, 15, 18, 24, 38, 47, 54, 60]
# observação: se a lista não tiver ordenada em ordem cresecente o comando lista.sort deve ser utilizado

def buscabinaria(lista,chave):
    pos_inic = 0
    pos_final = len(lista) - 1
    
    while pos_inic <= pos_final:
        pos_mid = (pos_inic + pos_final)//2 # obs // divide nosso número e pega apenas a parte inteira
        
        if chave == lista[pos_mid]:
            return pos_mid
        if chave < lista[pos_mid]:
            pos_final = pos_mid - 1  # -1 economiza processo
        if chave > lista[pos_mid]:
            pos_inic = pos_mid + 1 # +1 economiza uma casa a ser analizada (economiza processo)
            
    return print("A chave",chave, "não se encontra na lista")

quicksort(lista, 0, len(lista) - 1)
print(lista)
buscabinaria(lista,14)
        
'''----------------------------------------------------------------------------'''
''' Exercício prático 1: NAO FINALIZADO
    Iremos refazer as funções de busca sequencial e busca binária
assumindo que a lista possui chaves que podem ocorrer
múltiplas vezes na lista. Neste caso, retornaremos uma
lista com todas as posições onde a chave foi encontrada. Se a
chave não for encontrada na lista, retornaremos uma lista vazia.'''


lista = [1, 5, 10, 13, 15, 13, 24, 38, 13, 54, 60]
quicksort(lista, 0, len(lista) - 1)
print(lista)
chave = 13 # essa é nossa chave repetida

def buscaSequencial(lista, chave): 
    indice = 0
    indices = []
    for número in lista:
        if número != chave:
            indice = indice + 1
        elif número == chave:
            indices.append(indice)
            indice = indice + 1
        else:
            return print(indices)
    return print("A chave",chave, "não se encontra na lista")


buscaSequencial(lista, 13)



