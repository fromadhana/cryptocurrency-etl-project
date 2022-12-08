"""
    author: f.romadhana@gmail.com

"""
import os
import requests
import pandas as pd #type: ignore
from dotenv import load_dotenv #type: ignore
from bs4 import BeautifulSoup as bs #type: ignore
from sqlalchemy import create_engine #type: ignore

class BtcDist:

    def get_btcd(self):

        #get html from bitinfocharts
        url = 'https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html'
        r = requests.get(url)
        soup = bs(r.text, 'lxml')

        #get table of BTC Distribution
        table_btcd = soup.find('table', {'class':'table table-condensed bb'})

        #get header of BTC Distribution
        headers = []
        for i in table_btcd.find_all('th'):
            title = i.text.strip(', ')
            headers.append(title)

        #create BTC Distribution Dataframe
        btcd_df = pd.DataFrame(columns=headers)

        #get data of BTC Distribution
        for row in table_btcd.find_all('tr')[1:]:
            data = row.find_all('td')
            row_data = [td.text.strip() for td in data]
            length = len(btcd_df)
            btcd_df.loc[length] = row_data

        btcd_df.rename(columns={'Balance, BTC': "balance(btc)", 'Addresses': "address",
                                '% Addresses (Total)': "address_total(%)", 'Coins': "coins",
                                'USD': "usd", '% Coins (Total)':"coins_total(%)"}, inplace=True)

        try:
            # define database env
            load_dotenv()
            URL         = os.environ['url']
            USER        = os.environ['usr']
            PASSWORD    = os.environ['pas']
            PORT        = os.environ['por']
            DATABASE    = os.environ['dbs']

            # postgresql connection initiation
            conn_db = create_engine('postgresql://{usr}:{pasx}@{url}:{port}/{db}'.format(
                                    usr=USER, pasx=PASSWORD, url=URL, port=PORT, db=DATABASE))

            # insert all dataframe to postgresql database
            btcd_df.to_sql("btc_distribution", conn_db, if_exists='replace', index=False)

            print("Success insert table to postgresql! Good Job!")

        except: 
            print("Failed to proceed, please check again!")