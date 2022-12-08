"""
    author: f.romadhana@gmail.com

"""
import os
import datetime as dt
import pandas as pd #type: ignore
from dotenv import load_dotenv #type: ignore
from pandas import json_normalize #type: ignore
from sqlalchemy import create_engine #type: ignore
from pycoingecko import CoinGeckoAPI # type: ignore

class CoinApi:

    def get_coin(self):

        # create a client API
        cg = CoinGeckoAPI()

        # get coin list from API
        coin_list   = cg.get_coins_list()
        coinlist_df = pd.DataFrame.from_dict(coin_list).reset_index(drop=True)

        # get currency list from API
        currency_list   = cg.get_supported_vs_currencies()
        currencylist_df = pd.DataFrame.from_dict(currency_list).reset_index(drop=True)

        # get exchanges list from API
        exchanges_list   = cg.get_exchanges_id_name_list()
        exchangeslist_df = pd.DataFrame.from_dict(exchanges_list).reset_index(drop=True)

        # get asset platform from API
        asset_platform   = cg.get_asset_platforms()
        assetplatform_df = pd.DataFrame.from_dict(asset_platform).reset_index(drop=True)

        # get coin category from API
        coin_categories   = cg.get_coins_categories()
        coincategories_df = pd.DataFrame.from_dict(coin_categories).reset_index(drop=True)

        # get NFT list from API
        nft_list    = cg.get_nfts_list()
        nftlist_df  = pd.DataFrame.from_dict(nft_list).reset_index(drop=True)

        # get coin market ranks from API
        market_rank     = cg.get_coins_markets(vs_currency="usd")
        marketrank      = pd.DataFrame.from_dict(market_rank).reset_index(drop=True)
        marketrank_df   = marketrank.drop(columns=['market_cap_change_24h', 
                                        'market_cap_change_percentage_24h', 
                                        'ath_change_percentage', 
                                        'atl_change_percentage', 'roi'])

        # get BTC historical data from API
        btc_history     = cg.get_coin_market_chart_by_id(id="bitcoin", vs_currency="usd", days="max")
        btchistory_df   = pd.DataFrame(data=btc_history["prices"], columns=["date", "price"])
        ## reformat date
        btchistory_df["date"] = btchistory_df["date"].apply(
                                lambda x: dt.datetime.fromtimestamp(x / 1000).strftime("%m-%d-%Y"))

        # get BTC exchange rates from API
        exchange_rates   = cg.get_exchange_rates()
        exchangerates    = pd.DataFrame(exchange_rates["rates"])
        exchangerates_df = exchangerates.transpose()
 
        # get public companies BTC holdings from API
        public_btc   = cg.get_companies_public_treasury_by_coin_id(coin_id="bitcoin")
        publicbtc_df = pd.json_normalize(public_btc, "companies")

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
            coinlist_df.to_sql("coin_list", conn_db, if_exists='replace', index=False)
            currencylist_df.to_sql("currency_list", conn_db, if_exists='replace', index=False)
            exchangeslist_df.to_sql("exchanges_list", conn_db, if_exists='replace', index=False)
            assetplatform_df .to_sql("asset_platform", conn_db, if_exists='replace', index=False)
            coincategories_df.to_sql("coin_categories", conn_db, if_exists='replace', index=False)
            nftlist_df.to_sql("nft_list", conn_db, if_exists='replace', index=False)
            marketrank_df.to_sql("market_rank", conn_db, if_exists='replace', index=False)
            btchistory_df.to_sql("btc_history", conn_db, if_exists='replace',index=False)
            exchangerates_df.to_sql("exchange_rates", conn_db, if_exists='replace', index=False)
            publicbtc_df.to_sql("btc_hodler", conn_db, if_exists='replace', index=False)
        
            print("Success insert data to postgresql! Good Job!")
        
        except: 
            print("Failed to proceed, please check again!")