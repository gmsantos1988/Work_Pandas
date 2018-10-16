## O que é PANDAS?
`PANDAS` Pandas é uma biblioteca do Python que permite trabalhar com manipulação e análise de dados de forma simples e com alta performance.
 O nome Pandas é derivado de Word Panel Data
 
 ## Quais as funcionalidades do PANDAS?
- Rápido e eficiente para criação de objetos dataframe com indexação padrão e personalizada.
- Ferramentas para carregar em memoria objetos de dados de diferentes formatos de arquivos.
- Alinhamento de dados e manipulação integrada de dados.
- Remodelando e dinamizando conjunto de dados.
- Label baseado em etiqueta, indexação e subconjuntos de grandes conjuntos de dados.
- Colunas de estrutura de dados podem ser deletadas ou inseridas.
- Group by de dados para agregação e transformação.
- Alta performance para merging e joining de dados.
- Funcionalidade de séries temporais.

## Quais as funcionalidades do PANDAS?
Pode se instalar usando o Pacote de instalação Pip, usando:
	Pip install pandas

## Quais tipos de estrutura o Pandas trabalha ?

Series, Panel e DataFrame.

## Exemplo de Series:
Serie é uma Matriz unidimensional, capaz de armazenar dados de qualquer tipo (inteiro, string, float, objetos python, etc...).
```python
>>> import pandas as pd
>>> import numpy as np
>>> data = np.array(['um','dois','tres','quatro'])
>>> s = pd.Series(data)
>>> print(s)

## Exemplo de Series:
Serie é uma Matriz unidimensional, capaz de armazenar dados de qualquer tipo (inteiro, string, float, objetos python, etc...).
```python
>>> import pandas as pd
>>> import numpy as np
>>> data = np.array(['um','dois','tres','quatro'])
>>> s = pd.Series(data)
>>> print(s)

Lembramos que a serie pode ser construída através não só de matrizes, como de dicionários e elementos inputados manualmente com seus respectivos índices.

## Exemplo de DataFrame:
DataFrame é uma estrutura de dados bidimensional, ou seja, os dados são alinhados de maneira tabular. Esta estrutura pode ser construída através dos seguintes parâmetros: pandas.DataFrame( data, index, columns, dtype, copy).
```python
>>> import pandas as pd
>>> import numpy as np
>>> data = [['Alex',10],['Bob',12],['Clarke',13]]
>>> df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
>>> print (df)

## Exemplo de Panel:
Um panel é um contêiner 3D de dados. O termo dados do panel é derivado da econometria e é parcialmente responsável pelo nome pandas - pan (el) -da (ta) -s. Esta estrutura pode ser construída através dos seguintes parâmetros: pandas.Panel(data, items, major_axis, minor_axis, dtype, copy).
```python
>>> import pandas as pd
>>> import numpy as np
>>> data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
>>> p = pd.Panel(data)
>>> print(p['Item1'])

## Reindexação no Pandas:
A reindexação altera os labels de linha e os labels de coluna de um DataFrame.
Reindexar significa conformar os dados para corresponder a um determinado conjunto de rótulos ao longo de um determinado eixo.
A seguir segue um exemplo que utiliza um outro DataFrame para reindexar o outro:
```python
>>> import pandas as pd
>>> import numpy as np
>>> df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3']) 
>>> df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
>>> df1 = df1.reindex_like(df2)
>>> print (df1)

## Sorting com o Pandas:
Há duas maneiras disponíveis para realizar sorting:
Por Label e por valor atual.
Usando o método sort_index (), passando os argumentos do eixo e a ordem de classificação, o DataFrame pode ser classificado. 
Por padrão, a classificação é feita nos labels de linha em ordem crescente:
```python
>>> import pandas as pd
>>> import numpy as np
>>> unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])
>>> sorted_df=unsorted_df.sort_index()
>>> print (sorted_df)

Por valor
Como a classificação de índice, sort_values () é o método de classificação por valores.
Ele aceita um argumento 'by' que usará o nome da coluna do DataFrame com o qual os valores devem ser classificados.

>>> unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
>>> sorted_df = unsorted_df.sort_values(by='col1')
>>> print (sorted_df)

## Agregação em DataFrame:
```python
>>> import pandas as pd
>>> import numpy as np
>>> df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('10/10/2018', periods=10),
      columns = ['A', 'B', 'C', 'D'])
>>> print (df)
>>> r = df.rolling(window=3,min_periods=1)
>>> print( r['A'].aggregate([np.sum,np.mean]))

## A operação groupby envolve uma das seguintes operações no objeto original
- Dividindo o Objeto.
- Aplicando uma função.
- Combinando os resultados.
Em muitas situações, dividimos os dados em conjuntos e aplicamos algumas funcionalidades em cada subconjunto.
Na funcionalidade apply, podemos executar as seguintes operações:
- Agregação - computando uma estatística.
- Transformação - execute alguma operação específica do grupo.
- Filtragem - descartando os dados com alguma condição.

```python
>>> import pandas as pd
>>> import numpy as np
>>> ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
>>> df = pd.DataFrame(ipl_data)
>>> print (df.groupby(['Team','Year']).groups)

## Merge e Joins DataFrame:

 O Pandas possui operações de joins na memória de alto desempenho e recursos completos, muito semelhantes aos bancos de dados relacionais, como o SQL.
 
 Pandas fornece uma única função, merge, como o ponto de entrada para todas as operações de junção de banco de dados padrão entre os objetos DataFrame. Através dos seguintes parâmetros:

```python
>>>pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,left_index=False, right_index=False, sort=True).

>>> import pandas as pd
>>> import numpy as np
>>> left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
>>> right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
>>> print (pd.merge(left, right, on='subject_id', how='inner'))





