import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from IPython.display import display
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split

iris = sns.load_dataset('iris')
iris.species = iris.species.astype('category')
iris.info()

X = iris.copy()
X = X.drop(['species'], axis = 1)
y = iris.species.copy()

#usando 20% dos dados para teste e 80% para treino
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
