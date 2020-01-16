import numpy as np
import matplotlib as plt
from sklearn import datasets, tree
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import datasets, tree
from sklearn.metrics import accuracy_score,precision_score ,recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn import datasets
import pandas as pd 
from sklearn import preprocessing

df = pd.DataFram({ 'x1': np.random.chisquare(8,10000), \
                    'x2':np.random.beta(8,2,1000)*40,\
                    'x3': np.random.normal(50,3,10000) })

