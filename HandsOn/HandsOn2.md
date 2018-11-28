# Hands On 2

Utilizando o mesmo exemplo do Desafio 1, agora com Pandas.

``` python
import pandas as pd

notas = pd.Series([2,7,5,10,6])
print("Valores: ", notas.values)

notas = pd.Series([2,7,5,10,6], index=["Wilfred", "Abbie", "Harry", "Julia", "Carrie"])
print('Harry:', notas["Harry"])
print("Média:", notas.mean())
```