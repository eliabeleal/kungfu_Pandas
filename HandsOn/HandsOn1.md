# Hands On 1

 Um conceito muito utilizado em Pandas é o de array. Então nesse exemplo, vamos demonstrar como poderíamos agrupar um conjunto de notas. Dizer de quem são e por último fazer uma média.

``` python
notas = [2,7,5,10,6]
print("Valores:", notas)

notas = [{"Wilfred":2, "Abbie":7, "Harry":5, "Julia":10, "Carrie":6}]
print("Harry: {}".format(notas[0]["Harry"]))

m = 0

for i in notas[0]:
    m += notas[0][i]

print("Média: {}".format(m/len(notas[0])))
```