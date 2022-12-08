"""
    author: f.romadhana@gmail.com

"""

import os
import pandas as pd  # type: ignore
from dotenv import load_dotenv  # type: ignore
from pandas import json_normalize  # type: ignore
from pycoingecko import CoinGeckoAPI  # type: ignore
from sqlalchemy import create_engine  # type: ignore

class CoinDetail:

    def __init__(self, coins):
        self.coins = coins
    
    def get_detail(self): 

        # create a client API
        cg = CoinGeckoAPI()

        # get coin details from API
        coin_detail = cg.get_coin_by_id(id = self.coins,
                                        localization=False,
                                        tickers=False,
                                        market_data=False,
                                        comunity_data=True,
                                        developer_data=False,
                                        sparkline=False)
        #json normalize
        coindetail_df = pd.json_normalize(coin_detail)
        coindetail_df = coindetail_df[['id', 'symbol', 'name',
                                        'description.en', 'categories',
                                        'links.homepage', 'links.blockchain_site',
                                        'country_origin', 'genesis_date', 
                                        'market_cap_rank','coingecko_score', 
                                        'liquidity_score', 'links.twitter_screen_name',
                                        'community_data.twitter_followers', 
                                        'image.thumb', 'last_updated'
                                        ]]
        # rename columns
        coindetail_df.columns = ['id','symbol', 'name', 'description', 'categories',
                                'homepage', 'blockchain_site', 'origin',
                                'genesis_date', 'marketcap_rank', 'cg_score',
                                'liquid_score',  'twitter', 'twitter_followers',
                                'thumbnails', 'last_updated'
                                ]
        
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
            coindetail_df.to_sql("coin_details", conn_db, if_exists='append', index=False)

            print("insert coin details of " + self.coins)
                
        except:
            print("can't insert coin details of " + self.coins)

# insert coin list to retrieve coin details
CoinDetail('bitcoin').get_detail()
CoinDetail('ethereum').get_detail()
CoinDetail('tether').get_detail()
CoinDetail('usd-coin').get_detail()
CoinDetail('binancecoin').get_detail()
CoinDetail('binance-usd').get_detail()
CoinDetail('ripple').get_detail()
CoinDetail('dogecoin').get_detail()
CoinDetail('cardano').get_detail()
CoinDetail('matic-network').get_detail()
CoinDetail('polkadot').get_detail()
CoinDetail('staked-ether').get_detail()
CoinDetail('dai').get_detail()
CoinDetail('shiba-inu').get_detail()
CoinDetail('solana').get_detail()
CoinDetail('okb').get_detail()
CoinDetail('tron').get_detail()
CoinDetail('uniswap').get_detail()
CoinDetail('litecoin').get_detail()
CoinDetail('avalanche-2').get_detail()
CoinDetail('wrapped-bitcoin').get_detail()
CoinDetail('leo-token').get_detail()
CoinDetail('chainlink').get_detail()
CoinDetail('cosmos').get_detail()
CoinDetail('ethereum-classic').get_detail()
CoinDetail('the-open-network').get_detail()
CoinDetail('monero').get_detail()
CoinDetail('stellar').get_detail()
CoinDetail('bitcoin-cash').get_detail()
CoinDetail('algorand').get_detail()
CoinDetail('crypto-com-chain').get_detail()
CoinDetail('quant-network').get_detail()
CoinDetail('near').get_detail()
CoinDetail('vechain').get_detail()
CoinDetail('filecoin').get_detail()
CoinDetail('flow').get_detail()
CoinDetail('terra-luna').get_detail()
CoinDetail('chiliz').get_detail()
CoinDetail('hedera-hashgraph').get_detail()
CoinDetail('frax').get_detail()
CoinDetail('internet-computer').get_detail()
CoinDetail('chain-2').get_detail()
CoinDetail('elrond-erd-2').get_detail()
CoinDetail('eos').get_detail()
CoinDetail('trust-wallet-token').get_detail()
CoinDetail('paxos-standard').get_detail()
CoinDetail('apecoin').get_detail()
CoinDetail('tezos').get_detail()
CoinDetail('the-sandbox').get_detail()
CoinDetail('theta-token').get_detail()
CoinDetail('lido-dao').get_detail()
CoinDetail('true-usd').get_detail()
CoinDetail('aave').get_detail()
CoinDetail('decentraland').get_detail()
CoinDetail('axie-infinity').get_detail()
CoinDetail('bitcoin-cash-sv').get_detail()
CoinDetail('compound-usd-coin').get_detail()
CoinDetail('kucoin-shares').get_detail()
CoinDetail('usdd').get_detail()
CoinDetail('gemini-dollar').get_detail()
CoinDetail('whitebit').get_detail()
CoinDetail('bittorrent').get_detail()
CoinDetail('tokenize-xchange').get_detail()
CoinDetail('huobi-token').get_detail()
CoinDetail('maker').get_detail()
CoinDetail('iota').get_detail()
CoinDetail('pancakeswap-token').get_detail()
CoinDetail('ecash').get_detail()
CoinDetail('aptos').get_detail()
CoinDetail('osmosis').get_detail()
CoinDetail('gatechain-token').get_detail()
CoinDetail('zcash').get_detail()
CoinDetail('radix').get_detail()
CoinDetail('klay-token').get_detail()
CoinDetail('pax-gold').get_detail()
CoinDetail('btse-token').get_detail()
CoinDetail('arweave').get_detail()
CoinDetail('neo').get_detail()
CoinDetail('fantom').get_detail()
CoinDetail('the-graph').get_detail()
CoinDetail('cdai').get_detail()
CoinDetail('havven').get_detail()
CoinDetail('tether-gold').get_detail()
CoinDetail('mina-protocol').get_detail()
CoinDetail('evmos').get_detail()
CoinDetail('ethereum-pow-iou').get_detail()
CoinDetail('compound-ether').get_detail()
CoinDetail('nexo').get_detail()
CoinDetail('curve-dao-token').get_detail()
CoinDetail('dash').get_detail()
CoinDetail('thorchain').get_detail()
CoinDetail('kava').get_detail()
CoinDetail('xdce-crowd-sale').get_detail()
CoinDetail('basic-attention-token').get_detail()
CoinDetail('ethereum-name-service').get_detail()
CoinDetail('1inch').get_detail()
CoinDetail('bitdao').get_detail()
CoinDetail('dydx').get_detail()
CoinDetail('blockstack').get_detail()
CoinDetail('gmx').get_detail()