import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from IPython.display import display
warnings.filterwarnings("ignore")

titanic = sns.load_dataset('titanic')
titanic.survived = titanic.survived.astype('boolean')
display(titanic.head())

q3 = titanic.query('age > 27 and survived == True')
display(q3.head())