"""
    author: f.romadhana@gmail.com

"""
#import library
import numpy as np
import pandas as pd
import pickle
import re
import datetime as dt
from datetime import datetime
import pandas as pd 
from pycoingecko import CoinGeckoAPI
import streamlit as st
import imageio as iio

image = iio.imread('btc.png')
st.image(image)
st.write("""
-----------------------------------------------------
""")
st.caption("#NFA - Not Financial Advice")

# CoinGecko client API
cg = CoinGeckoAPI()
# get BTC historical data from API
btc_ohlc= cg.get_coin_ohlc_by_id(id="bitcoin", vs_currency="usd", days="max")
btc_df  = pd.DataFrame(data = btc_ohlc, columns = ['Date', 'Open', 'High' ,'Low', 'Close'])
#reformat date
btc_df['Date'] = btc_df['Date'].apply(lambda x: dt.datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d'))
btc_df.set_index('Date', inplace=True)
# bitcoin history data
#st.date_input("Please select date to retrieve historical data", dt.date(2022,12,7))
x = st.selectbox(
    'Please select sample historical data',
    ("2022-12-07","2022-12-03", "2022-11-30")
)
btc_df.loc[x]

#import .pickle
pickle_in = open('btc_prediction_lr.pkl', 'rb')
lin_reg = pickle.load(pickle_in)

st.markdown("Now, please input the Open, High & Low Price for predict the ₿itcoin's Close price!")
Open = st.number_input('Open Price', min_value=0)
High = st.number_input('High Price',min_value=0)
Low = st.number_input('Low Price',min_value=0)

prediction = lin_reg.predict([[Open, High, Low]])
predict = np.array2string(prediction, precision=0, suppress_small=True)
pre = re.sub(r"[\([{.})\]]", "", predict) 
pre_print = "₿itcoin's Close Price will be $ " + pre

if Open == 0.00 :
    st.warning("Please input Open, High & Low Price", icon="⚠️")
elif st.button("Predict ₿itcoin's Close Price"):
    st.success(pre_print, icon="🚀")
    st.button("Clear")
else:
    pass