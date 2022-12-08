"""
    author: f.romadhana@gmail.com

"""
from apps import (BtcDist, BtcRich)

try:
    p1 = BtcDist().get_btcd()
    p2 = BtcRich().get_richest()
    p1.join()
    p2.join()
except TypeError:
    print('== This is the end of inserting crypto data ==')