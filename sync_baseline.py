__author__ = "Puri Phakmongkol"
__author_email__ = "me@puri.in.th"

"""
* Sky dragon project
*
* Created date : 30/09/2023
*
+      o     +              o
    +             o     +       +
o          +
    o  +           +        +
+        o     o       +        o
-_-_-_-_-_-_-_,------,      o
_-_-_-_-_-_-_-|   /\_/\
-_-_-_-_-_-_-~|__( ^ .^)  +     +
_-_-_-_-_-_-_-""  ""
+      o         o   +       o
    +         +
o      o  _-_-_-_- Async_test : Sync for baseline
    o           +        
+      +     o        o      +
https://realpython.com/async-io-python/
"""

import time
import asyncio
import functools

from tvDatafeed import TvDatafeed, Interval

import pandas as pd

def tv_sync(stock_list) :
    tv = TvDatafeed()
    re_data = {}
    for _ in stock_list :
        print(_)
        data = tv.get_hist(symbol=_, 
                    exchange='SET',
                    interval=Interval.in_1_hour,
                    n_bars=1000)
        re_data[_] = data

    return re_data

if __name__ == '__main__' :
    # stock_list = ['ADVANC', 'PTT', 'AOT', 'AP', 'JAS', 'JASIF', 'OR', 'TRUE', 'MAKRO']
    stock_df = pd.read_csv('data/set50_stock_list.csv')
    stock_list = list(stock_df['symbol'])
    s = time.perf_counter()
    data = tv_sync(stock_list)
    elapsed = time.perf_counter() - s
    print(data)
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')
