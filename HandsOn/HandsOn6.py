# Histograma
df["preco"].plot.hist()
# 30 bins (partes) e linhas pretas
df["preco"].plot.hist(bins=30, edgecolor='black')
# barras
df["bairro"].value_counts().plot.bar()
df["bairro"].value_counts().plot.barh()
# Titulos
df["bairro"].value_counts().plot.barh(title="Número de apartamentos")
# Dispersão
df.plot.scatter(x='preco', y='area')
# Styles
plt.style.use('ggplot')
plt.style.available
# pizza
df["quartos"].value_counts().plot.pie()
# Tamanho dos pontos
df.plot.scatter(x='preco', y='area', s=.5)
# Tamnho da amostra
df.sample(frac=.1).plot.scatter(x='preco', y='area')


