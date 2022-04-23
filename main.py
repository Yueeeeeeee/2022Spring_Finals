import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from utils import *


def main(file_path='./data/master.csv'):
    data = pd.read_csv(file_path)
    data = data[data['year'] < 2015]
    df0 = data[['year', 'suicides_no']]
    df0 = df0.groupby(['year'], as_index=False).agg({'suicides_no': 'sum'})
    df1 = data[['year', 'sex', 'suicides_no']]
    df1 = df1.groupby(['year', 'sex'], as_index=False).agg({'suicides_no': 'sum'})
    df2 = data[['year', 'age', 'suicides_no']]
    df2 = df2.groupby(['year', 'age'], as_index=False).agg({'suicides_no': 'sum'})
    df2_1 = df2[df2['age']=='5-14 years']
    df2_2 = df2[df2['age']=='15-24 years']
    df2_3 = df2[df2['age']=='25-34 years']
    df2_4 = df2[df2['age']=='35-54 years']
    df2_5 = df2[df2['age']=='55-74 years']
    df2_6 = df2[df2['age']=='75+ years']
    young = pd.concat([df2_1, df2_2]).groupby(['year'], as_index=False).agg({'suicides_no': 'sum'})
    adult = pd.concat([df2_3, df2_4]).groupby(['year'], as_index=False).agg({'suicides_no': 'sum'})
    old = pd.concat([df2_5, df2_6]).groupby(['year'], as_index=False).agg({'suicides_no': 'sum'})
    adult_old = pd.concat([df2_3, df2_4, df2_5, df2_6]).groupby(['year'], as_index=False).agg({'suicides_no': 'sum'})
    all_age = pd.concat([df2_1, df2_2, df2_3, df2_4, df2_5, df2_6]).groupby(['year'], as_index=False).agg({'suicides_no': 'sum'})

    sns.set(style="ticks")
    sns.set_context({"figure.figsize": (24, 10)})
    colors = sns.color_palette("Blues_d")

    #Plot 1 - background - "total" (all) series
    sns.barplot(x = all_age['year'], y = all_age['suicides_no'], color=colors[5])

    #Plot 2 - overlay - "middle" (adult + old) series
    middle_plot = sns.barplot(x = adult_old['year'], y = adult_old['suicides_no'], color=colors[3])

    #Plot 3 - overlay - "bottom" (old) series
    bottom_plot = sns.barplot(x = old['year'], y = old['suicides_no'], color=colors[1])


    topbar = plt.Rectangle((0, 0), 1, 1, fc=colors[5], edgecolor='none')
    middlebar = plt.Rectangle((0, 0), 1, 1, fc=colors[3], edgecolor='none')
    bottombar = plt.Rectangle((0, 0), 1, 1, fc=colors[1],  edgecolor='none')
    l = plt.legend([bottombar, middlebar, topbar], ['Over 54', 'Age 25-54', 'Under 25'], loc=1, ncol=2, prop={'size':14})
    l.draw_frame(False)

    sns.despine(left=True)
    bottom_plot.set_ylabel("Total Suisides")
    bottom_plot.set_xlabel("Year")
    plt.suptitle('Suicide Age Distribution vs. Year', fontsize=20)
    plt.show()

    sns.set(style="ticks")
    sns.set_context({"figure.figsize": (24, 10)})
    colors = sns.color_palette("Blues_d")

    #Plot 1 - background - "total" series
    sns.barplot(x = df0['year'], y = df0['suicides_no'], color=colors[5])

    #Plot 2 - overlay - "bottom" series
    bottom_plot = sns.barplot(x = df1[df1['sex']=='male']['year'], y = df1[df1['sex']=='male']['suicides_no'], color=colors[3])


    topbar = plt.Rectangle((0, 0), 1, 1, fc=colors[5], edgecolor='none')
    bottombar = plt.Rectangle((0, 0), 1, 1, fc=colors[3],  edgecolor='none')
    l = plt.legend([bottombar, topbar], ['Male', 'Female'], loc=1, ncol = 2, prop={'size':14})
    l.draw_frame(False)

    sns.despine(left=True)
    bottom_plot.set_ylabel("Total Suisides")
    bottom_plot.set_xlabel("Year")
    plt.suptitle('Suicide Gender Distribution vs. Year', fontsize=20)
    plt.show()
    
    #for item in ([bottom_plot.xaxis.label, bottom_plot.yaxis.label] +
    #             bottom_plot.get_xticklabels() + bottom_plot.get_yticklabels()):
    #    item.set_fontsize(16)


if __name__ == "__main__":
    main()