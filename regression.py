import numpy as np
from scipy import stats
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *


def compute_correlation(df, column1, column2):
    assert column1 in df.columns
    assert column2 in df.columns
    col1 = df[[column1]].values.squeeze()
    col2 = df[[column2]].values.squeeze()
    col1 = normalize(col1)
    col2 = normalize(col2)
    return stats.pearsonr(col1, col2)


def regression_analysis(df, *columns):
    print('Correlation Analysis using', columns)
    columns = list(columns)
    reg = linear_model.LinearRegression()
    reg.fit(df[columns], df['Rate'])
    preds = reg.predict(df[columns])
    if 'Predictions' in df.columns:
        df['Predictions'] = preds
    else:
        df.insert(df.shape[1], 'Predictions', preds)
    
    r, sig = compute_correlation(df, 'Rate', 'Predictions')
    mse = np.square(df[['Predictions']].values.squeeze(),
            df[['Rate']].values.squeeze()).mean()
    
    print('Suicide Rate and Prediction Correlation: {:.4f}'.format(r))
    print('Suicide Rate and Prediction P-value: {:.4f}'.format(sig))
    print('Suicide Rate and Prediction MSE: {:.4f}'.format(mse))
    return df


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

    if savepath is not None:
        plt.savefig(savepath)
    
    plt.show()


if __name__ == "__main__":
    rates = get_rates(return_dict=False)
    hours = get_hours(return_dict=False)
    prods = get_prods(return_dict=False)
    gdp = get_gdp(return_dict=False)
    wages = get_wages(return_dict=False)
    welfare = get_welfare(return_dict=False)
    latitude = get_latitude(return_dict=False)
    sunshine = get_sunshine(return_dict=False)
    df = combine_dataframe(rates, hours, prods, wages, gdp, welfare, latitude, sunshine)

    visualize(df, 'Hours', 'Rate', savepath='hours_rate.png')
    visualize(df, 'Productivity', 'Rate', savepath='prod_rate.png')
    visualize(df, 'GDP', 'Rate', savepath='gdp_rate.png')
    visualize(df, 'Wages', 'Rate', savepath='wages_rate.png')
    visualize(df, 'Welfare', 'Rate', savepath='welfare_rate.png')
    visualize(df, 'Latitude', 'Rate', savepath='lat_rate.png')
    visualize(df, 'Sunshine', 'Rate', savepath='sun_rate.png')

    regression_analysis(df, 'Hours')
    regression_analysis(df, 'Productivity')
    regression_analysis(df, 'GDP')
    regression_analysis(df, 'Wages')
    regression_analysis(df, 'Welfare')
    regression_analysis(df, 'Latitude')
    regression_analysis(df, 'Sunshine')
    
    regression_analysis(df, 'Hours', 'Productivity')
    regression_analysis(df, 'GDP', 'Wages')
    regression_analysis(df, 'Latitude', 'Sunshine')
    regression_analysis(df, 'Hours', 'Productivity', 'GDP', 'Wages', 'Welfare', 'Latitude', 'Sunshine')