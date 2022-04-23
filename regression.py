import numpy as np
import pandas as pd
import pycountry
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict
from scipy import stats
from sklearn import linear_model
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *


rates = get_rates(return_dict=False)
hours = get_hours(return_dict=False)
prods = get_prods(return_dict=False)
gdp = get_gdp(return_dict=False)
welfare = get_welfare(return_dict=False)
latitude = get_latitude(return_dict=False)
sunshine = get_sunshine(return_dict=False)
df = combine_dataframe(rates, hours, prods, gdp, welfare, latitude, sunshine)



def compute_correlation(df, column1, column2):
    assert column1 in df.columns
    assert column2 in df.columns
    col1 = df[[column1]].values.squeeze()
    col2 = df[[column2]].values.squeeze()
    col1 = normalize(col1)
    col2 = normalize(col2)
    return stats.pearsonr(col1, col2)


def visualize(df, column1, column2, regression=True, savepath=None):
    sns.set(style="ticks")
    sns.set_context({"figure.figsize": (8, 5)})

    col1 = df[[column1]].values.squeeze()
    col2 = df[[column2]].values.squeeze()
    plt.plot(col1, col2, 'o')

    if regression:
        sns.regplot(col1, col2)
    if column2 == 'Rate':
        column2 = 'Suicide Rate'
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(column1 + ' vs. ' + column2)
    plt.show()

    if savepath is not None:
        plt.savefig(savepath)


compute_correlation(df, 'Rate', 'Hours')
visualize(df, 'Hours', 'Rate')

# correlation = stats.pearsonr(normalize(data_pic2['Hours']), normalize(data_pic2['Rate']))
# print('Pearson Correlation between Annual Working Hours and Suicide Rate is:', correlation)
# plt.plot(data_pic2['Hours'], data_pic2['Rate'], 'o')
# plt.xlabel('Annual Working Hours')
# plt.ylabel('Suicide Rate')
# plt.title('Suicide Rate vs. Working Hours')
# plt.show()
    
# correlation = stats.pearsonr(normalize(data_pic2['Productivity']), normalize(data_pic2['Rate']))
# print('Pearson Correlation between Productivity and Suicide Rate is:', correlation)
# plt.plot(data_pic2['Productivity'], data_pic2['Rate'], 'o')
# plt.xlabel('Productivity')
# plt.ylabel('Suicide Rate')
# plt.title('Suicide Rate vs. Productivity')
# plt.show()

# reg = linear_model.LinearRegression()
# reg.fit(data_pic2[['Hours', 'Productivity']], data_pic2['Rate'])
# y = reg.predict(data_pic2[['Hours', 'Productivity']])
# correlation1 = stats.pearsonr(normalize(y), normalize(data_pic2['Rate']))
# print('Pearson Correlation between Hours + Productivity and Suicide Rate is:', correlation1)