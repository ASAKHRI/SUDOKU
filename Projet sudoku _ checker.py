import numpy as np
import pandas as pd

# Creation of DataFrames
a=np.random.randint(1,10, size=(3,3)) 
a_df = pd.DataFrame(a)
b=np.random.randint(1,10, size=(3,3))
b_df = pd.DataFrame(b)
c=np.random.randint(1,10, size=(3,3))
c_df = pd.DataFrame(c)
d=np.random.randint(1,10, size=(3,3))
d_df = pd.DataFrame(d)
e=np.random.randint(1,10, size=(3,3))
e_df = pd.DataFrame(e)
f=np.random.randint(1,10, size=(3,3))
f_df = pd.DataFrame(f)
g=np.random.randint(1,10, size=(3,3))
g_df = pd.DataFrame(g)
h=np.random.randint(1,10, size=(3,3))
h_df = pd.DataFrame(h)
i=np.random.randint(1,10, size=(3,3))
i_df = pd.DataFrame(i)


#
concat_a_b = pd.concat([a_df,b_df],axis=1,ignore_index = True)
concat_a_b_c = pd.concat([concat_a_b,c_df],axis=1,ignore_index=True)
concat_a_b_c_d = pd.concat([d_df,e_df,f_df],axis=1,ignore_index=True)
concat_a_b_c_d=concat_a_b_c_d.reset_index(drop=True)
concat_a_b_c_d_1 = pd.concat([concat_a_b_c,concat_a_b_c_d],axis=0,ignore_index=True)
concat_g_h_i = pd.concat([g_df,h_df,i_df],axis=1,ignore_index=True)


concat_a_b_c_d = concat_a_b_c_d.loc[~concat_a_b_c_d.index.duplicated(keep='first')]
concat_g_h_i = concat_g_h_i.loc[~concat_g_h_i.index.duplicated(keep='first')]

concat_final = pd.concat([concat_a_b_c_d_1,concat_g_h_i],axis=0,ignore_index=True)
print(concat_final)

df_compact = [a_df,b_df,c_df,d_df,e_df,f_df,g_df,h_df,i_df]

def check_column(concat_final) : 
    for i in range(9):
        return concat_final[i].is_unique   

def check_row(concat_final) : 
    for j in range(9):
        return concat_final.loc[j].is_unique

def arr_tolist(arr):
    arr_list = arr.tolist()
    return arr_list

def set_list(arr_list): 
    arr_set = set(arr_list)
    return arr_set

def test_arr(arr_set):
    return len(arr_set) == 9
    