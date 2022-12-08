"""
    author: f.romadhana@gmail.com

"""

from apps import (CoinApi, CoinDetail)

try:
    p1 = CoinApi().get_coin() 
    p2 = CoinDetail().get_detail()
    p1.join()
    p2.join()
except TypeError:
    print('== This is the end of inserting crypto data ==')