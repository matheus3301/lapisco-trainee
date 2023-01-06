import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from IPython.display import display
warnings.filterwarnings("ignore")

df1 = pd.DataFrame({
    'a': [1,2,3],
    'b': [10,11,12]
})

df2 = pd.DataFrame({
    'a': [4,5,6],
    'b': [13,14,15]
})

df1['data_from'] = 'dataframe 1'
df2['data_from'] = 'dataframe 2'


df3 = pd.concat([df1,df2], ignore_index=True)
df3.species = df3.data_from.astype('category')

display(df3)
