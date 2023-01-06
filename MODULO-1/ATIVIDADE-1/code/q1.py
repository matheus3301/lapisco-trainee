import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from IPython.display import display
warnings.filterwarnings("ignore")

iris = sns.load_dataset('iris')
iris.species = iris.species.astype('category')
iris.head()

cols = ['sepal_length','sepal_width','petal_length','petal_width']
for index, col in enumerate(cols):
    print(f"--- Outliers para a coluna: {col} ---")
    
    upper_limit = iris[col].mean() + np.abs(3 * iris[col].std())
    lower_limit = iris[col].mean() - np.abs(3 * iris[col].std())
    
    query = f"{col} > {upper_limit:.2f} | {col} < {lower_limit:.2f}"
    
    outliers = iris.query(query)
    
    # se nao encontrei outliers, crio eles
    if outliers.empty:
        print("\nOutliers nao encontrados, gerando outliers\n")
        
        #criando outlier
        new_row = {}
        for new_col in cols:
            new_row[new_col] = 0
        
        new_row[col] = upper_limit + 1.0
        new_row['species'] = 'setosa'        
        
        #inserindo outlier no dataframe
        iris = iris.append(new_row, ignore_index = True)

        outliers = iris.query(query)
                
    display(outliers)
    print("\n\n\n")
    

