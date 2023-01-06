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

def person_type(age: int) -> str:
    if age < 18:
        return 'Child'
    if age < 65:
        return 'Adult'
    return 'Old'

titanic['person_type'] = [person_type(age) for age in titanic.age]
sample = titanic.sample(n=10, random_state=1)

display(sample)