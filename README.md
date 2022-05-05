# 2022 Spring Final Project: Analysis on Socio-Economic and Geographical Factors that Affect Suicide Rate

IS 597 PRO Final Projet: Analysis on Socio-Economic and Geographical Factors that Affect Suicide Rate
by Zhenrui Yue, Huimin Zeng, Mengfei Lan

<img src=media/intro_trend.png>
<img src=media/intro_distribution.png>


# Analysis

Hypothesis 1. Poor working conditions are positively related with suicide rate.

Hypothesis 2. Economic development is negatively related to suicide rate.

Hypothesis 3. Social Welfare could reduce the probability of suicide. 

Hypothesis 4. Warm and sunny climate could reduce the probability of suicide. 

We first analyze main data to extract suicide trends and distributions. The analysis results can be visualized with our main file.

To investigate the hypotheses, we use collect country-specifc data (e.g., GDP, wages, latitude etc.) and compute their correlations to the suicide rate. For example, the correlation between GDP per capita and suicide rate is 0.1821 with a p-value of 0.3269, suggesting GDP per capita is not significantly correlated with suicide. Such analysis can be found in our regression file. We additionally visualize each investigated factor in the visualization files.

Based on our analysis results, our conclusions are:

1. We reject the first 3 hypotheses “Poor working conditions are positively related with suicide rate.”, “Economic development is negatively related to suicide rate.” and “Social Welfare could reduce the probability of suicide.”

2. We accept the hypothesis “Warm and sunny climate could reduce the probability of suicide.”. Specifically, sunshine hours is the most important single factor with correlation r=0.5600 and p-value=0.0011.

3. Additionally, we observe highest statistical significance by performing regression analysis among all factors and the suicide rate with correlation r=0.5940 and p-value=0.0004.


## Usage

Demo can be found in demo.ipynb, which contains the majority of our analysis code and visualization.

Regression analysis is in regression.py, which contains the necessary code to analyze and compute correlation.

Main file generates the trends and distributions of the main data used in our analysis, 2 figures are generated in main file.

Visualization files (visualization1.py etc.) utilize plotly to generate country-specific visualization in a web browser.

File utilities are in utils.py, we have a main function which loads, combines and print the data files.

An example:
```
python regression.py
```


## Data & Requirements

Our data can be downloaded [here](https://drive.google.com/file/d/1DdnFGsSwA2ljzoZdS74ZNuacWskO4Cc0/view?usp=sharing).

Please download data and unzip all files to the data (i.e., ./data/) folder.

To run our code you need the following data, we manually collect some of them. The running environment can be found in requirements.txt. Contact us if you need more details on our data or env.

[1] https://en.wikipedia.org/wiki/Suicide_in_the_United_States

[2] https://en.wikipedia.org/wiki/Loneliness

[3] http://apps.who.int/gho/data/node.main.MHSUICIDEASDR?lang=en

[4] https://blogs.cdc.gov/niosh-science-blog/2018/09/13/suicide-prevention

[5] https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016

[6] https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate

[7] https://en.wikipedia.org/wiki/Working_time

[8] https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_hour_worked

[9] https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita

[10] https://data.oecd.org/earnwage/average-wages

[11] https://en.wikipedia.org/wiki/List_of_countries_by_social_welfare_spending

[12] https://en.wikipedia.org/wiki/List_of_national_capitals_by_latitude

[13] https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration