# Análise de dados com Pandas

## 1. Python e análise de dados

A simplicidade do Python é uma característica que o faz tão atraente para desenvolvedores. E ela tem sido ótima para preparação de dados. Contudo, apesar de todo o seu poder, sua criptonita é (era… Spoiler) a análise de dados. Os analistas precisavam migrar para outra linguagem que favorecia isso, o R por exemplo.

Para nosso minicurso precisaremos do [Python 3.6](https://www.python.org/downloads/release/python-367/) ou [Python 3.7](https://www.python.org/downloads/release/python-371/).

Depois de instalar, veja se ele está acessível:

```sh
python3 -V
```

Vamos precisar também do gerenciador de pacotes do Python, pip:

```sh
python3 -m pip install --upgrade pip
```

_Caso você esteja usando o Ubuntu 16:_

```sh
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
python3 -m pip install --upgrade pip
```

Vamos ver como seria uma simples análise de dados com python:

### Challenge one

* abra o terminal e crie a pasta minicurso_pandas

```sh
mkdir minicurso_pandas
```

* entre nela

```sh
cd minicurso_pandas
```

* crie o ch1.py

```sh
code ch1.py
```

O comando code irá abrir o editor de texto Visual Studio Code

* codifique:

1. crie uma estrutura onde o índice de cada elemento sejam os alunos: Wilfred, Abbie, Harry, Julia e Carrie.

2. atribua para cada um dos alunos as seguites notas, sequencialmente: 2, 7, 5, 10 e 6

3. imprima a nota de Harry (5)

4. faça uma média das notas

* volte para o terminal e digite

```sh
python3 ch1.py
```

Conseguiu?

Veja o [code](HandsOn/HandsOn1.md)

## 2. Pandas

Pandas é uma biblioteca open source que fornece estruturas de dados de alto desempenho e fáceis de usar, assim como ferramentas de análise de dados para a linguagem de programação Python. O Kung Fu (trabalho duro) fica com o Pandas você só tem que saber o que quer fazer. E este é o propósito desse curso, te introduzir no mundo da análise de dados com conceitos básicos.

### Clonando a pasta do minicurso

* dentro da pasta de nosso minicurso, vamos clonar o repositório do github

```sh
git clone https://github.com/elileal/kungfu_Pandas
```

* entre na pasta kungfu_Pandas

```sh
cd kungfu_Pandas/
```

* execute o seguinte comando:

```sh
python3 HandsOn/HandsOn2.py
```

Essa é a mesma saída do nosso _challenge one_, mas como seria o [code](HandsOn/HandsOn2.md) dele?

**Compare com o nosso primeiro desafio, é mais simples, ou melhor, Pytônico?**

Antes de iniciarmos com o Pandas, precisamos instalar as bibliotecas e dependências para o nosso minicurso

* dentro da pasta kungfu_Pandas, abra o terminal e digite

```sh
pip install -r requirements.txt
```

### [Anaconda](https://www.anaconda.com/what-is-anaconda/)

O Anaconda é uma plataforma que auxilia na preparação do ambiente necessário para o trabalho com análise de dados e ciência de dados. Que pode ser uma alternativa ao nosso _requirements_. Você pode acessar o site e baixar ou usar **wget**:

32 bits version:

```sh
wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86.sh
```

64 bits version

```sh
wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh
```

* execute

32 bits:

```sh
bash Anaconda-5.3.1-Linux-x86.sh
```

64 bits:

```sh
bash Anaconda3-5.3.1-Linux-x86_64.sh
```

## 3. Estrutura de dados base do Pandas

* Serie - Uma Serie é como um array unidimensional, uma lista de valores. Toda Serie possui um índice, que dá o rótulo a cada elemento da lista.

Vamos evoluir nosso desafio, se você ainda não o fez, tente, mas se já fez, refatore-o usando Pandas baseado no último code.

Adicione estas [linhas](HandsOn/HandsOn3_1.md) depois da última linha. Perceba a simplicidade dos comandos.

* Data Frame - Já um DataFrame é uma estrutura bidimensional de dados, como uma planilha.

A manipulação de um Data Frame é tão simples quanto a de uma Série. Copie essas [linhas](HandsOn/HandsOn3_2.md) e cole no seu **ch1.py**.

## 4. Tipos de entrada de dados usados

### Com CSV: **pd.read_csv()**

* no seu terminal digite

```sh
python3
```

agora você está no terminal do Python

* importe as bibliotecas

```py
>>> import pandas as pd
```

* carregue o CSV com os dados

```py
>>> df = pd.read_csv("Dados/dados.csv")
```

* imprima os dados

```py
>>> df
```

* vamos ver as 5 primeiras linhas

```py
>>> df.head()
```

* você pode dizer quantas linhas

```py
>>> df.head(n=10)
```

* valores únicos

```py
>>> df["bairro"].unique()
```

[Esse](HandsOn/HandsOn4.md) arquivo mostra mais comando para os Data Frames

**experimente o comando pd.read_\<TAB>.**

## 5. Visualização de dados

Incluído no Pandas, temos os métodos de visualização do matplotlib, usado para exploração rápida de dados.

Nessa fase, precisamos do jupyter notebook, uma aplicação web que pode ajudar a entender e visualizar dados e resultados de análises, juntamente com o código.

* digite no seu terminal

```sh
jupyter notebook
```

* no canto superior direito, clique em _new_ e depois em _Python 3_

* execute os próximos dois exemplos

1. [Condomínios RJ](HandsOn/HandsOn5_1.md)

    Antes de continuar, baixe esse [arquivo](https://drive.google.com/file/d/1UAOM6xkuiK5XBEed2load-yOvpvFgYSk/view?usp=sharing)

2. [Exemplo usado no Curso do professor Masanori](exemploMasanori.ipynb)

## 6. Salvando tudo

De forma pytônica, [salvar](HandsOn/HandsOn6.md) seu DataFrame é tão simples quanto carregá-lo

## 7. Challenges

Vamos praticar tudo que vimos até aqui com os [**DESAFIOS**](Desafios/desafios.md)

## 8. Agradecimentos

Ao professor [Fernando Masanori](https://about.me/fmasanori) pela palestra na Python Brasil\[14]. A grande inspiração desse minicurso.

Ao professor [Luiz Carlos](https://github.com/lucachaves) por acreditar que esse minicurso seria possível.

Ao meu amigo [Neil Prado](https://github.com/neilprado) por topar esse desafio

Ao [IfTech](http://joaopessoa.ifpb.edu.br/iftech/) pela oportunidade de compartilhar esse apredizado 
