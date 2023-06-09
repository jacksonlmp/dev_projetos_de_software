import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Carregar a base de dados Wine
wine = load_wine()
X = wine.data
y = wine.target

# Dividir os dados em treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciar o classificador KNN
knn = KNeighborsClassifier(n_neighbors=3)

# Treinar o classificador
knn.fit(X_treino, y_treino)

# Fazer previsões no conjunto de teste
y_predito = knn.predict(X_teste)

# Calcular as métricas de avaliação
acuracia = accuracy_score(y_teste, y_predito)
precisao = precision_score(y_teste, y_predito, average='weighted')
recall = recall_score(y_teste, y_predito, average='weighted')

# Imprimir as métricas
print("Acurácia:", acuracia)
print("Precisão:", precisao)
print("Recall:", recall)

# Contar a quantidade de acertos e erros para cada classe
classes = wine.target_names
corretos = np.zeros(len(classes))
incorretos = np.zeros(len(classes))

for i in range(len(y_teste)):
    if y_teste[i] == y_predito[i]:
        corretos[y_teste[i]] += 1
    else:
        incorretos[y_teste[i]] += 1

# Criar um gráfico de barras com os acertos e erros para cada classe
x = np.arange(len(classes))
largura = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - largura/2, corretos, largura, label='Acertos')
rects2 = ax.bar(x + largura/2, incorretos, largura, label='Erros')

ax.set_xlabel('Classes')
ax.set_ylabel('Quantidade')
ax.set_title('Resultados do KNN na base Wine')
ax.set_xticks(x)
ax.set_xticklabels(classes)
ax.legend()

fig.tight_layout()
plt.show()
