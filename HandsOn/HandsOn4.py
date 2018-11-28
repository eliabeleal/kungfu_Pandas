#Hands on 4
df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})
print(df)
# Tipos de objetos
print(df.dtypes)
# Ver as colunas
print(df.columns)
# Acessando os valores
print(df["Seminário"])

print(df.describe())
# Ordenando
print(df.sort_values(by="Seminário"))
# Localizando dados pelo índice, existem várias outras formas de fazer isso
print(df.loc[3])
# Boolean Indexing
print(df[df["Seminário"] > 8.0])
# bitwise (&, |, ~)
print(df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)])

