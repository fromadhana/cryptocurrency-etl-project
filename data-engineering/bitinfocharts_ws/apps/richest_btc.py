"""
    author: f.romadhana@gmail.com

"""
import os
import requests
import pandas as pd #type: ignore
from dotenv import load_dotenv #type: ignore
from bs4 import BeautifulSoup as bs #type: ignore
from sqlalchemy import create_engine #type: ignore

class BtcRich:

    def __init__(self, pages):
        self.pages = pages
    
    def get_richest(self):

        #get html from bitinfocharts
        url = f'https://bitinfocharts.com/top-100-richest-bitcoin-addresses-{self.pages}.html'
        r = requests.get(url)
        soup = bs(r.text, 'lxml')

        #get table of top richest btc addresses
        tb1 = soup.find('table', {'class':'table table-striped abtb'})
        tb2 = soup.find('table', {'class':'table table-striped bb'})

        #get header of top richest btc addresses
        headers = []
        for i in tb1.find_all('th'):
            title = i.text.strip('△1w/△1m ')
            headers.append(title)

        #create btc distribution dataframe
        tb_1 = pd.DataFrame(columns=headers)
        tb_2 = pd.DataFrame(columns=headers)

        #get data table 1
        for row1 in tb1.find_all('tr')[1:]:
            data1 = row1.find_all('td')
            row_data1 = [td.text.strip() for td in data1]
            length1 = len(tb_1)
            tb_1.loc[length1] =row_data1

        #get data table 2
        for row2 in tb2.find_all('tr')[::1]:
            data2 = row2.find_all('td')
            row_data2 = [td.text.strip() for td in data2]
            length2 = len(tb_2)
            tb_2.loc[length2] =row_data2
        
        #combine 2 tables into 1 dataframe
        full_table = [tb_1, tb_2]
        result = pd.concat(full_table)

        #rename all column name
        result.rename(columns={'': "ranks", 'Address': "address", 'Balance': "balance",
                                '% of coins': "no_of_coins(%)", 'First In': "first_in",
                                'Last In': "last_in", 'Ins': "coin_ins",
                                'First Out': "first_out", 'Last Out': "last_out",
                                'Outs': "coin_outs"}, inplace=True)
        
        
        try:
            # load dotenv                                       
            load_dotenv()
            # define database env
            URL         = os.environ['url']
            USER        = os.environ['usr']
            PASSWORD    = os.environ['pas']
            PORT        = os.environ['por']
            DATABASE    = os.environ['dbs']

            # postgresql connection initiation
            conn_db = create_engine('postgresql://{usr}:{pasx}@{url}:{port}/{db}'.format(
                                    usr=USER, pasx=PASSWORD, url=URL, port=PORT, db=DATABASE))

            # insert dataframe to postgresql database
            result.to_sql("richest_btc", conn_db, if_exists='append', index=False)

            print("insert pages " + self.pages + " success!")
                
        except:
            print("can't insert pages " + self.pages + ", please check again!")

        
#get all pages
BtcRich('1').get_richest()
BtcRich('2').get_richest()
BtcRich('3').get_richest()
BtcRich('4').get_richest()
BtcRich('5').get_richest()
BtcRich('6').get_richest()
BtcRich('7').get_richest()
BtcRich('8').get_richest()
BtcRich('9').get_richest()
BtcRich('10').get_richest()
BtcRich('11').get_richest()
BtcRich('12').get_richest()
BtcRich('13').get_richest()
BtcRich('14').get_richest()
BtcRich('15').get_richest()
BtcRich('16').get_richest()
BtcRich('17').get_richest()
BtcRich('18').get_richest()
BtcRich('19').get_richest()
BtcRich('20').get_richest()
BtcRich('21').get_richest()
BtcRich('22').get_richest()
BtcRich('23').get_richest()
BtcRich('24').get_richest()
BtcRich('25').get_richest()
BtcRich('26').get_richest()
BtcRich('27').get_richest()
BtcRich('28').get_richest()
BtcRich('29').get_richest()
BtcRich('30').get_richest()
BtcRich('31').get_richest()
BtcRich('32').get_richest()
BtcRich('33').get_richest()
BtcRich('34').get_richest()
BtcRich('35').get_richest()
BtcRich('36').get_richest()
BtcRich('37').get_richest()
BtcRich('38').get_richest()
BtcRich('39').get_richest()
BtcRich('40').get_richest()
BtcRich('41').get_richest()
BtcRich('42').get_richest()
BtcRich('43').get_richest()
BtcRich('44').get_richest()
BtcRich('45').get_richest()
BtcRich('46').get_richest()
BtcRich('47').get_richest()
BtcRich('48').get_richest()
BtcRich('49').get_richest()
BtcRich('50').get_richest()
BtcRich('51').get_richest()
BtcRich('52').get_richest()
BtcRich('53').get_richest()
BtcRich('54').get_richest()
BtcRich('55').get_richest()
BtcRich('56').get_richest()
BtcRich('57').get_richest()
BtcRich('58').get_richest()
BtcRich('59').get_richest()
BtcRich('60').get_richest()
BtcRich('61').get_richest()
BtcRich('62').get_richest()
BtcRich('63').get_richest()
BtcRich('64').get_richest()
BtcRich('65').get_richest()
BtcRich('66').get_richest()
BtcRich('67').get_richest()
BtcRich('68').get_richest()
BtcRich('69').get_richest()
BtcRich('70').get_richest()
BtcRich('71').get_richest()
BtcRich('72').get_richest()
BtcRich('73').get_richest()
BtcRich('74').get_richest()
BtcRich('75').get_richest()
BtcRich('76').get_richest()
BtcRich('77').get_richest()
BtcRich('78').get_richest()
BtcRich('79').get_richest()
BtcRich('80').get_richest()
BtcRich('81').get_richest()
BtcRich('82').get_richest()
BtcRich('83').get_richest()
BtcRich('84').get_richest()
BtcRich('85').get_richest()
BtcRich('86').get_richest()
BtcRich('87').get_richest()
BtcRich('88').get_richest()
BtcRich('89').get_richest()
BtcRich('90').get_richest()
BtcRich('91').get_richest()
BtcRich('92').get_richest()
BtcRich('93').get_richest()
BtcRich('94').get_richest()
BtcRich('95').get_richest()
BtcRich('96').get_richest()
BtcRich('97').get_richest()
BtcRich('98').get_richest()
BtcRich('99').get_richest()