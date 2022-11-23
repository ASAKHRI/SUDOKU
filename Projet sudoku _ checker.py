import numpy as np
import pandas as pd


a=np.random.randint(1,10, size=(3,3)) 
a_df = pd.DataFrame(a)
a_df = a_df.loc[~a_df.index.duplicated(keep='first')]
a_df

b=np.random.randint(1,10, size=(3,3))
b_df = pd.DataFrame(b)
b_df

c=np.random.randint(1,10, size=(3,3))
c_df = pd.DataFrame(c)
c_df[0].is_unique

d=np.random.randint(1,10, size=(3,3))
d_df = pd.DataFrame(d)
e=np.random.randint(1,10, size=(3,3))
e_df = pd.DataFrame(e)
f=np.random.randint(1,10, size=(3,3))
f_df = pd.DataFrame(f)