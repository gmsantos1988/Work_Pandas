#Trabalhando com DataFrame no Pandas
import pandas as pd
import numpy as np
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)