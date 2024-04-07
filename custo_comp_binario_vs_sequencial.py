''' Vamos comparar o custo computacional dos dois códigos desenvolvidos nos programas anteriores:
    O código de busca sequencial e o binário'''
    
''' A função custo do código de busca sequencial se deu por [3n + 3] - O(n) - onde n é o número de iterações
    realizadas no nosso sistema. Em contrapartida,a função custo do nosso código de busca binária, se deu
    por [6*int(log2(n)) + 6] - O(log2(n)). A seguir, vamos comparar ambas funções colocando o custo computacional em 
    função do número de elementos da nossa matriz.
    Vale ressaltar que ambas as fórmulas foram obtidas para o pior dos casos,onde o elemento a ser achado 
    é o último da lista no caso da busca sequencial e o primeiro ou último, no caso da busca binária'''
    
import numpy as np
import matplotlib.pyplot as plt 

def custo_binario(n): # nos retornará uma matriz com os as quantidade de iterações associados aos elementos impostos
    iteracoes = []
    for i in range (0,len(n)):
        iteracoes.append(6*int(np.log(n[i])) + 6)
    print(iteracoes)
    return iteracoes


def custo_sequencial(n):
    iteracoes = []
    for i in range (0,len(n)):
        iteracoes.append(3*n[i] + 3)
    print(iteracoes)
    return iteracoes

''' Plotando a comparação entre os dois gráficos'''
xpoints = np.array([10,50,100,300,500,1000]) # quantidade de elementos na matriz
ybinpoints = custo_binario(xpoints) # número de iterações no caso binário
yseqpoints = custo_sequencial(xpoints) # número de iterações no caso sequencial

plt.xlabel('Tamanho da nossa matriz') 
plt.ylabel("Número de iterações")
plt.title('Custo computacional - busca sequencial(red) vs busca binária (blue)')
plt.plot(xpoints, ybinpoints, 'o:b') 
plt.plot(xpoints, yseqpoints, 'o:r')
plt.show()


