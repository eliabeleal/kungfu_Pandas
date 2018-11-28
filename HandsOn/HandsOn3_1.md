# Hands On 3.1

Uma vantagem do Pandas é a simplicidade dos comandos e sua integração com outras bibliotecas. Abaixo mostramos como exibir os índices da Série que criamos, algumas análises e o uso da lib numpy com Pandas.

``` python
print("Notas index:", notas.index)
print("Desvio padrão:", notas.std())
print(notas.describe())

import numpy as np
print(notas**2)
print(np.log(notas))
```