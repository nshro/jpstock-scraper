from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from scipy import stats

ma_day = [10, 20, 50]

def create_dframe(company_id, start_year, end_year, url, headers):
    data = []
    for year in range(start_year, end_year+1):
        result = requests.get(url+company_id+'/'+str(year)+'/', headers=headers).content
        soup = BeautifulSoup(result)
        summary = soup.find('div', {'class':'table_wrap'})
        if not summary:
            continue
        tables = summary.find_all('table')

        rows = tables[0].find_all('tr')

        for tr in rows:
            d = []
            cols = tr.find_all('td')
            for td in cols:
                text = td.find(text=True)
                d.append(text)
            if not d == []:
                data.append(d)

    df = pd.DataFrame(data, dtype=np.float32)
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df = df.set_index('Date')

    add_ma(df)
    add_drets(df)

    return df

def add_ma(company_df, ma_day=ma_day):
    for ma in ma_day:
        column_name = "MA {}".format(str(ma))
        company_df[column_name] = company_df['Adj Close'].rolling(window=ma).mean()

def add_drets(company_df):
    company_df['Daily Return'] = company_df['Adj Close'].pct_change()

def df_plot(dfs, columns, start, end, linestyle=None, marker=None):
    for df in dfs:
        for col in columns:
            df[start:end][col].plot(subplots=False, figsize=(10,4))
    plt.xlim(start, end)
    plt.show()

def plot_ma(dfs, start, end, ma_day=ma_day):
    columns = ['Adj Close']
    for ma in ma_day:
        column_name = "MA {}".format(str(ma))
        columns.append(column_name)
    df_plot((dfs), columns, start, end)

def plot_rets(dfs, start, end):
    df_plot((dfs), ['Daily Return'], start, end, '--', 'o')