#Hands on 2
import pandas as pd
notas = pd.Series([2,7,5,10,6])
print("Valores: ", notas.values)
notas = pd.Series([2,7,5,10,6], index=["Wilfred", "Abbie", "Harry", "Julia", "Carrie"])
print('Harry:', notas["Harry"])
print("Média:", notas.mean())

