import numpy as np
import pandas as pd
import plotly.express as px
import pycountry
from collections import defaultdict


OECD = ['MEX', 'KOR', 'GRC', 'IND', 'CHL', 'RUS', 'POL', 'LVA', 'ISR', 'ISL', 'IRL', \
        'EST', 'PRT', 'USA', 'CZE', 'HUN', 'NZL', 'SVK', 'ITA', 'JPN', 'CAN', 'ESP', \
        'SVN', 'GBR', 'AUS', 'FIN', 'SWE', 'AUT', 'CHE', 'BEL', 'LUX', 'FRA', 'NLD', \
        'NOR', 'DNK', 'DEU']



def normalize(x):
    return (x - np.mean(x)) / np.std(x)


source = px.data.gapminder()
source = source[['country', 'iso_alpha']].drop_duplicates().values
COUNTRY_DICT = defaultdict(str)
for i in range(len(source)):
    COUNTRY_DICT[source[i][0]] = source[i][1]
for country in pycountry.countries:
    COUNTRY_DICT[country.name] = country.alpha_3


COUNTRY_DICT['Antigua and Barbuda'] = 'ATG'
COUNTRY_DICT['Bahamas'] = 'BHS'
COUNTRY_DICT['Barbados'] = 'BRB'
COUNTRY_DICT['Belize'] = 'BLZ'
COUNTRY_DICT['Luxembourg'] = 'LUX'
COUNTRY_DICT['Malta'] = 'MLT'
COUNTRY_DICT['Republic of Korea'] = 'KOR'
COUNTRY_DICT['Saint Lucia'] = 'LCA'
COUNTRY_DICT['Saint Vincent and Grenadines'] = 'VCT'
COUNTRY_DICT['Seychelles'] = 'SYC'
COUNTRY_DICT['Suriname'] = 'SUR'
COUNTRY_DICT['Turkmenistan'] = 'TKM'
COUNTRY_DICT['Ukraine'] = 'UKR'
COUNTRY_DICT['Russia'] = 'RUS'
COUNTRY_DICT['Ivory Coast'] = 'CIV'
COUNTRY_DICT['South Korea'] = 'KOR'
COUNTRY_DICT['Cape Verde'] = 'CPV'
COUNTRY_DICT['Moldova'] = 'MDA'
COUNTRY_DICT['Bolivia'] = 'BOL'
COUNTRY_DICT['F.S. Micronesia'] = 'FSM'
COUNTRY_DICT['North Korea'] = 'PRK'
COUNTRY_DICT['Slovak Republic'] = 'SVK'
COUNTRY_DICT['Czech Republic'] = 'CZE'
COUNTRY_DICT['Tanzania'] = 'TZA'
COUNTRY_DICT['Laos'] = 'LAO'
COUNTRY_DICT['Vietnam'] = 'VNM'
COUNTRY_DICT['East Timor'] = 'TMP'
COUNTRY_DICT['Brunei'] = 'BRU'
COUNTRY_DICT['Iran'] = 'IRN'
COUNTRY_DICT['Venezuela'] = 'VEN'
COUNTRY_DICT['São Tomé and Príncipe'] = 'STP'
COUNTRY_DICT['Syria'] = 'SYR'
COUNTRY_DICT['DR Congo'] = 'COD'


COUNTRY_DICT_LOWER = defaultdict(str)
for k, v in COUNTRY_DICT.items():
    COUNTRY_DICT_LOWER[k.lower()] = v


def clean_country_string(code):
    code = code.replace('(more info)', '')
    code = code.replace('[a]', '')
    code = code.replace('\xa0', '').strip()
    return code


def map_to_country_code(code):
    country_code = ''
    if code in COUNTRY_DICT.keys():
        country_code = COUNTRY_DICT[code]
    elif code.lower() in COUNTRY_DICT_LOWER.keys():
        country_code = COUNTRY_DICT_LOWER[code.lower()]
    return country_code


def transform_to_dict(df):
    out_dict = {}
    keys = df[['Code']].values.squeeze()
    for key in keys:
        out_dict[key] = df[df['Code']==key].squeeze()[-1]
    return out_dict


def get_rates(file_path='./data/rate.xlsx', return_dict=False):
    rates = pd.read_excel(file_path).values[:, 1:]
    data = []
    for i in range(len(rates)):
        country = rates[i][0]
        country = clean_country_string(country)
        country_code = map_to_country_code(country)
        country_rate = float(rates[i][2])
        if country_code != '':    
            data.append([country_code, country_rate])

    df = pd.DataFrame(data=data, columns=['Code', 'Rate'])
    if return_dict:
        return transform_to_dict(df)
    return df


def get_hours(file_path='./data/hours.xlsx', return_dict=False):
    hours = pd.read_excel(file_path).values
    data = []
    for i in range(len(hours)):
        country = hours[i][1]
        country = clean_country_string(country)
        country_code = map_to_country_code(country)
        country_hour = float(hours[i][3])    
        if country_code != '':  
            data.append([country_code, country_hour])

    df = pd.DataFrame(data=data, columns=['Code', 'Hours'])
    if return_dict:
        return transform_to_dict(df)
    return df


def get_prods(file_path='./data/prod.xlsx', return_dict=False):
    prods = pd.read_excel(file_path)
    df = prods.groupby(['Code'],as_index=False).agg({'Productivity': 'mean'})
    if return_dict:
        return transform_to_dict(df)
    return df


def get_wages(file_path='./data/wage.xlsx', return_dict=False):
    wages = pd.read_excel(file_path).values
    data = []
    for i in range(len(wages)):
        country = wages[i][1]
        country = clean_country_string(country)
        country_code = map_to_country_code(country)
        country_wage = float(wages[i][2])
        if country_code != '':  
            data.append([country_code, country_wage])

    df = pd.DataFrame(data=data, columns=['Code', 'Wages'])
    if return_dict:
        return transform_to_dict(df)
    return df


def get_gdp(file_path='./data/gdp.xlsx', return_dict=False):
    gdp = pd.read_excel(file_path).values
    data = []
    for i in range(len(gdp)):
        country = gdp[i][1]
        country = clean_country_string(country)
        country_code = map_to_country_code(country)
        country_gdp = float(gdp[i][2])
        if country_code != '':   
            data.append([country_code, country_gdp])
    
    df = pd.DataFrame(data=data, columns=['Code', 'GDP'])
    df.set_index('Code')
    if return_dict:
        return transform_to_dict(df)
    return df


def get_welfare(file_path='./data/welfare.xlsx', return_dict=False):
    welfare = pd.read_excel(file_path).values
    data = []
    for i in range(len(welfare)):
        country = welfare[i][1]
        country = clean_country_string(country)
        country_code = map_to_country_code(country)
        country_welfare = float(welfare[i][2])
        if country_code != '':   
            data.append([country_code, country_welfare])
    
    df = pd.DataFrame(data=data, columns=['Code', 'Welfare'])
    df.set_index('Code')
    if return_dict:
        return transform_to_dict(df)
    return df


def get_latitude(file_path='./data/latitude.xlsx', return_dict=False):
    latitude = pd.read_excel(file_path).values
    data = []
    for i in range(len(latitude)):
        country = latitude[i][1]
        country = clean_country_string(country)
        country_code = map_to_country_code(country)
        country_latitude = float(latitude[i][2])
        if country_code != '':   
            data.append([country_code, country_latitude])
        
    df = pd.DataFrame(data=data, columns=['Code', 'Latitude'])
    df = df.groupby(['Code'], as_index=False).agg({'Latitude': 'mean'})
    if return_dict:
        return transform_to_dict(df)
    return df


def get_sunshine(file_path='./data/sunshine.xlsx', return_dict=False):
    df = pd.read_excel(file_path)

    df = df.groupby(['Country'],as_index=False).agg({'Sunshine': 'mean'})
    df["Country"] = df["Country"].map(map_to_country_code)
    df.columns = ['Code', 'Sunshine']
    df.set_index('Code')
    if return_dict:
        return transform_to_dict(df)
    return df


def combine_dataframe(*dfs):
    df_out = dfs[0]
    for df in dfs[1:]:
        df_out = df_out.merge(df, on='Code')
    return df_out

if __name__ == "__main__":
    print(COUNTRY_DICT)
    print(COUNTRY_DICT_LOWER)
    rates = get_rates(return_dict=False)
    hours = get_hours(return_dict=False)
    prods = get_prods(return_dict=False)
    gdp = get_gdp(return_dict=False)
    welfare = get_welfare(return_dict=False)
    latitude = get_latitude(return_dict=False)
    sunshine = get_sunshine(return_dict=False)
    print(combine_dataframe(rates, hours, prods, gdp, welfare, latitude, sunshine))