# Hands On 4

 Com Pandas, temos muitas possibilidade de entrada de dados. Experimente a auto-completação de pd.read_\<TAB>. Utilizando o CSV, podemos visualizar de várias maneiras o nosso Data Frame.

``` python
# 5 primeiros
print(df.head())
# 10 primeiros
print(df.head(n=10))
# 5 últimos
print(df.tail())
# valores únicos
print(df["bairro"].unique())
# quantidades
print(df["bairro"].value_counts())
# percentual
print(df["bairro"].value_counts(normalize=True))
# groupby: agrupa as ocorrências
print(df.groupby("bairro").mean())
print(df.groupby("bairro").mean()["pm2"].sort_values())
# usando funções
def truncar(bairro):
    return bairro[:3]
print(df["bairro"].apply(truncar))
# lambda
print(df["bairro"].apply(lambda x: x[:3]))
```

A possibilidade de tratar dados incompletos é reconhecidamente uma das artes mais poderosas do Pandas. Quando em um dataset há algum tipo de incompletude dos dados, o Pandas preenche a lacuna com NaN (np.nan - é um valor especial definido no Numpy)

```python
print(df2 = df.head())
print(df2 = df2.replace({"pm2": {12031.25: np.nan}}))
print(df2.dropna())
print(df2.fillna(99))
print(df2.isna())
```