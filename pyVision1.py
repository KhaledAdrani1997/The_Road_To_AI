#dataset Synthetic Financial Datasets

import numpy as np 
import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm_notebook
import seaborn as sns
#%matplotlib inline 
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# init_notebook_mode(connected=True)

def missing_data(data):
    total = data.isnull().sum()
    percent = (data.isnull().sum()/data.isnull().count()*100)
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['Types'] = types
    return(np.transpose(tt))

def unique_values(data):
    total = data.count()
    tt = pd.DataFrame(total)
    tt.columns = ['Total']
    uniques = []
    for col in data.columns:
        unique = data[col].nunique()
        uniques.append(unique)
    tt['Uniques'] = uniques
    return(np.transpose(tt))

def plot_count(df, feature, title='', size=2): #used with one feature especially for categorical, counting the population
    f, ax = plt.subplots(1,1, figsize=(3*size,2*size))
    total = float(len(df))
    sns.countplot(df[feature],order = df[feature].value_counts().index, palette='Set3')
    plt.title(title)
    if(size > 2):
        plt.xticks(rotation=90, size=8)
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2.,
                height + 3,
                '{:1.4f}%'.format(100*height/total),
                ha="center") 
    plt.show()

def subplot_showfliers(x,y,hue,data_df,palette): #need more work here
    #fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16,12))
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,6))
    s = sns.boxplot(ax = ax1, x="isFraud", y="step", hue="isFraud",data=data_df, palette="PRGn",showfliers=True)
    s = sns.boxplot(ax = ax2, x="isFraud", y="step", hue="isFraud",data=data_df, palette="PRGn",showfliers=False)
    plt.show()


def walk_into_folder(path_folder): #I guess it shows all files included within this path; you can then copy the file
    #from kaggle standared kernel
    import os
    for dirname, _, filenames in os.walk(path_folder):
        for filename in filenames:
            print(os.path.join(dirname, filename))

def box_whisker_plots(data):
    data.plot(kind='box' , sharex = False , sharey = False, figsize=(15,10))

def histogram(data):
    data.hist(edgecolor = 'black', linewidth=1.2, figsize=(15,5))

def boxplot(data):
    data.boxplot(by="species",figsize=(15,10))

def pairplot_matrix(data):
    sns.pairplot(data, hue="species")



