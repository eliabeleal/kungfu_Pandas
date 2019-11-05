# Hands On 5.1

O método de visualização rápida de dados foi construído com base na lib matplotlib. Dando assim mais liberdade na visualização de dados.

```python
import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("Dados/dados.csv")
df["preco"].plot.hist()
df["preco"].plot.hist(bins=30, edgecolor='black')
df["bairro"].value_counts().plot.bar()
df["bairro"].value_counts().plot.barh()
df["bairro"].value_counts().plot.barh(title="Número de apartamentos")
df.plot.scatter(x='preco', y='area')
plt.style.use('ggplot')
plt.style.available
df["quartos"].value_counts().plot.pie()
df.plot.scatter(x='preco', y='area', s=.5)
df.sample(frac=.1).plot.scatter(x='preco', y='area')
```
