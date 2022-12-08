"""
    author: f.romadhana@gmail.com

"""

from apps import CoinApi

if __name__ == '__main__':
    run_data = CoinApi()
    run_data.get_coin()