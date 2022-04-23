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


def get_country_code(code):
    country_code = ''
    if code in COUNTRY_DICT.keys():
        country_code = COUNTRY_DICT[code]
    elif code.lower() in COUNTRY_DICT_LOWER.keys():
        country_code = COUNTRY_DICT_LOWER[code.lower()]
    return country_code


def get_rates(file_path='./data/rate.xlsx'):
    rates = pd.read_excel(file_path).values[:, 1:]
    data = []
    for i in range(len(rates)):
        country = rates[i][0]
        country = clean_country_string(country)
        country_code = get_country_code(country)
        country_rate = float(rates[i][2])    
        data.append([country_code, country_rate])

    df = pd.DataFrame(data=data, columns=['Code', 'Rate'])
    return df


def get_hours(file_path='./data/hours.xlsx'):
    hours = pd.read_excel(file_path).values
    data = []
    for i in range(len(hours)):
        country = hours[i][1]
        country = clean_country_string(country)
        country_code = get_country_code(country)
        country_hour = float(hours[i][3])    
        data.append([country_code, country_hour])

    df = pd.DataFrame(data=data, columns=['Code', 'Hours'])
    return df


if __name__ == "__main__":
    print(COUNTRY_DICT)
    print(COUNTRY_DICT_LOWER)
    print(get_hours())