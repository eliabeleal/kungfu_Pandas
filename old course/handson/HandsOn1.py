#Hands on 1
# Mostrando os valores, sem preparar os índices
notas = [2,7,5,10,6]
print("Valores:", notas)
# Para trabalhar com índices, é preciso usar o conceito de discionário, além disso o acesso a uma chave que nos interessa depende do índice do discionário.
notas = [{"Wilfred":2, "Abbie":7, "Harry":5, "Julia":10, "Carrie":6}]
print("Harry: {}".format(notas[0]["Harry"]))
# Para tirar uma média de todas as notas
m = 0
for i in notas[0]:
    m += notas[0][i]

print("Média: {}".format(m/len(notas[0])))

