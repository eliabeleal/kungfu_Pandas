# Comandos Data Frame usando o arquivo dados.csv
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
# NaN
print(df2 = df.head())
print(df2 = df2.replace({"pm2": {12031.25: np.nan}}))
print(df2.dropna())
print(df2.fillna(99))
print(df2.isna())
