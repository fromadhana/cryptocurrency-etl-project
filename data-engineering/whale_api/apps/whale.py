"""
    author: f.romadhana@gmail.com

"""
import os
import time
import json
import requests
import pandas as pd #type: ignore
import datetime as dt 
from dotenv import load_dotenv #type: ignore
from pandas import json_normalize #type: ignore
from sqlalchemy import create_engine #type: ignore

class WhaleApi:
    
    def get_alert(self):
        
        # load dotenv                                       
        load_dotenv()
        # define database env
        URL_DB      = os.environ['url']
        USER        = os.environ['usr']
        PASSWORD    = os.environ['pas']
        PORT        = os.environ['por']
        DATABASE    = os.environ['dbs']
        API_KEY     = os.environ['key']
        API_URL     = os.environ['bas']
     
        # current Unix timestamp minus time in seconds for retrieving transactions
        timestamp = int(time.time()) - 900  
        # min.USD value of transactions returned
        value     = "500000"  

        get_trans = requests.get(
                    f'{API_URL}api_key={API_KEY}&min_value={value}&start={timestamp}')
       
        # transform to json
        json_text = get_trans.json()

        # parsing json
        trans_df = pd.DataFrame(json_text['transactions'])
        
               
        mod_df   = trans_df.loc[:,['blockchain', 'symbol', 'id', 'transaction_type', 'hash', 
                    'from', 'to', 'timestamp', 'amount', 'amount_usd', 'transaction_count']]
 
        # json normalize list of dict
        listd     = mod_df.to_json(orient="records")
        whale_df  = pd.json_normalize(json.loads(listd))
        
        # reformat timestamp
        whale_df["timestamp"] = whale_df["timestamp"].apply(
                        lambda x: dt.datetime.fromtimestamp(x).strftime("%m-%d-%Y %H:%M:%S"))
       
        try:
            # postgresql connection initiation
            conn_db = create_engine('postgresql://{usr}:{pasx}@{url}:{port}/{db}'.format(
                                    usr=USER, pasx=PASSWORD, url=URL_DB, port=PORT, db=DATABASE))

            # insert dataframe to postgresql database
            whale_df.to_sql("whale_transactions", conn_db, if_exists='append', 
                            index=False, method='multi', chunksize=1000)

            # print timestamp execution
            now = whale_df.iloc[-1]['timestamp']
            print("----------------------------------")
            print("Running at ", now)
            print("----------------------------------")
            print("Success insert whale transactions!")
            print("----------------------------------")

        except:
            print("Can't insert whale transactions!")
            print("===============================")

        # print dataframe
        print("== Alert!!! Whale is moving! ==")
        print(whale_df)