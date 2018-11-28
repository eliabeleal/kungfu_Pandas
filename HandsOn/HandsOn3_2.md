# Hands On 3.2

A manipulação de um Data Frame é tão simples quanto a de uma Série. Abaixo podemos visualizar: os tipos de objetos, as colunas, acessar determinados valores, ordenar, localizar pelo índice, fazer uma indexação booleana e usar o conceito de bitwise (operações a nível de bits com números inteiros, sua representação binária).

``` python
df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})
print(df)
print(df.dtypes)
print(df.columns)
print(df["Seminário"])

print(df.describe())
print(df.sort_values(by="Seminário"))
print(df.loc[3])
print(df[df["Seminário"] > 8.0])
print(df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)])
```