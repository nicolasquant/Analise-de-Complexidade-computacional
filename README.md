### Visão geral
Este diretório contém implementações didáticas de algoritmos de busca (sequencial e binária), análises de complexidade com medição/plotagem, uma comparação de custos computacionais entre as duas abordagens e um notebook com uma implementação educativa de agrupamento tipo k-means usando o conjunto de dados Iris.

### Estrutura do diretório
```
/workspace
├── algoritmo de busca sequencial e binaria.py
├── analise_complexidade_binaria.py
├── analise_complexidade_sequencial.py
├── custo_comp_binario_vs_sequencial.py
├── kmeans.ipynb
└── README.md
```

### Pré-requisitos
- Python 3.10+
- Pacotes: numpy, matplotlib, scikit-learn (apenas para o notebook)

Instalação rápida dos pacotes:
```bash
python3 -m venv /workspace/.venv
source /workspace/.venv/bin/activate
pip install numpy matplotlib scikit-learn
```

### Como executar
- Busca sequencial e binária (demonstrações em console):
```bash
python3 "/workspace/algoritmo de busca sequencial e binaria.py"
```

- Análise de complexidade da busca sequencial (contagem de iterações, tempo e gráfico):
```bash
python3 /workspace/analise_complexidade_sequencial.py
```

- Análise de complexidade da busca binária (contagem de iterações, tempo e gráfico):
```bash
python3 /workspace/analise_complexidade_binaria.py
```

- Comparação de custo computacional (gráfico lado a lado):
```bash
python3 /workspace/custo_comp_binario_vs_sequencial.py
```

- Notebook k-means (Iris):
  - Abra no Jupyter local ou no Google Colab.
  - Localmente, após ativar o ambiente: `pip install jupyter` e `jupyter lab`.
  - No Colab, basta fazer upload do `kmeans.ipynb` e executar.

### O que cada arquivo faz
- algoritmo de busca sequencial e binaria.py
  - Implementa `quicksort` (para ordenar listas), `buscaSequencial` e `buscabinaria`.
  - Demonstra a busca sequencial e a binária em listas de exemplo.
  - Inclui uma versão da busca sequencial que retorna todas as posições quando a chave aparece várias vezes.
  - Observação: os índices exibidos no console são 1‑baseados (primeiro elemento = posição 1).

- analise_complexidade_sequencial.py
  - Gera listas de tamanhos distintos, ordena com `quicksort` (apenas para exibição), executa a busca sequencial no pior caso (elemento no fim).
  - Conta iterações aproximadas executadas e mede o tempo de execução.
  - Plota um gráfico ilustrativo da relação entre tamanho da lista e número de iterações.
  - Fórmula didática usada (pior caso): 3n + 3 → O(n).

- analise_complexidade_binaria.py
  - Ordena as listas com `quicksort` (pré‑requisito para a busca binária) e executa a busca binária no pior caso (extremos).
  - Conta iterações aproximadas, mede tempos e plota gráfico ilustrativo.
  - Fórmula didática usada (pior caso): 6*⌊log2(n)⌋ + 6 → O(log n).

- custo_comp_binario_vs_sequencial.py
  - Define funções de custo para cada algoritmo e plota um gráfico comparativo do número de iterações vs. tamanho da entrada.
  - Nota: para refletir logaritmo base 2, considere substituir `np.log` por `np.log2` na função de custo binário, se desejar alinhar estritamente à fórmula 6*log2(n) + 6.

- kmeans.ipynb
  - Usa o dataset Iris (scikit‑learn); divide em treino/teste e normaliza com `StandardScaler`.
  - Seleciona pontos iniciais aleatórios, agrupa por distância euclidiana e calcula pontos médios (centroides) uma vez.
  - Repete amostragens de inicializações e escolhe aquela com menor soma de variâncias intra‑grupo.
  - Plota a separação resultante. É uma implementação didática de k‑means (não iterativa completa como `sklearn.cluster.KMeans`).

### Fórmulas de complexidade (pior caso)
- Busca sequencial: 3n + 3 → O(n)
- Busca binária: 6*⌊log2(n)⌋ + 6 → O(log n)

### Notas e limitações
- As contagens de iterações são aproximações pedagógicas para ilustrar crescimento assintótico; valores absolutos dependem da implementação.
- O `quicksort` é usado para preparar a lista da busca binária; seu custo não está incluído na análise de custo da busca binária.
- Os gráficos requerem um backend gráfico; se estiver em ambiente sem GUI, use backends como `matplotlib.use("Agg")` para salvar em arquivo ao invés de `plt.show()`.
