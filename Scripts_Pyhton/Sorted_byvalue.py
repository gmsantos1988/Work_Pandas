#Trabalhando com aggr no Pandas
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('10/10/2018', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df)

r = df.rolling(window=3,min_periods=1)
print( r['A'].aggregate([np.sum,np.mean]))