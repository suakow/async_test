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
o      o  _-_-_-_- Async_test : Async using joblib
    o           +        
+      +     o        o      +
https://realpython.com/async-io-python/
"""

import time
import asyncio
import functools

from tvDatafeed import TvDatafeed, Interval
from joblib import Parallel, delayed

import pandas as pd
import numpy as np

tv = TvDatafeed()

def get_tv(_) :
    print(_)
    time.sleep(np.random.uniform(0,1))
    
    try :
        data = tv.get_hist(symbol=_, 
                            exchange='SET', 
                            interval=Interval.in_1_hour, 
                            n_bars=1000)
        return (_, data)
        
    except Exception as e:
        # print(e)
        return _
        # if 'Handshake status 429 Too Many Requests' in str(e) :
        #     time.sleep(np.random.uniform(0,1))
        #     print(f'retry at {_}')
        #     get_tv(_)

        # else :
        #     print('else', e)

if __name__ == '__main__' :
    # stock_list = ['ADVANC', 'PTT', 'AOT', 'AP', 'JAS', 'JASIF', 'BTS', 'TRUE', 'GULF']
    stock_df = pd.read_csv('data/set50_stock_list.csv')
    stock_list = list(stock_df['symbol'])
    s = time.perf_counter()
    p_data = Parallel(n_jobs=-1, prefer="threads")(delayed(get_tv)(_) for _ in stock_list)

    """Check pulling result"""
    re_data = {}
    while True :
        none_list = []
        for _ in p_data :
            if isinstance(_, str) :
                none_list.append(_)

            else :
               re_data[_[0]] = _[1]

        if len(none_list) == 0 :
            break

        else :
            print('retrying none..', none_list)
            p_data = Parallel(n_jobs=-1, prefer="threads")(delayed(get_tv)(_) for _ in none_list)

    elapsed = time.perf_counter() - s
    print(re_data)
    print(len(re_data))
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')
