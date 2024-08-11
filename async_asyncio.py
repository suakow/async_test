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
o      o  _-_-_-_- Async_test : Async using asyncio
    o           +        
+      +     o        o      +
https://realpython.com/async-io-python/
"""

import time
import asyncio
import functools

from tvDatafeed import TvDatafeed, Interval

import pandas as pd
import numpy as np

def tv_async(stock_list) :
    re_data = {}
    tv = TvDatafeed()

    def get_tv(_) :
        print(_)
        time.sleep(np.random.uniform(0,1))
        try :
            data = tv.get_hist(symbol=_, 
                               exchange='SET', 
                               interval=Interval.in_1_hour, 
                               n_bars=1000)
            re_data[_] = data
            
        except Exception as e:
            # print(e)
            # re_data[_] = _
            if 'Handshake status 429 Too Many Requests' in str(e) :
                time.sleep(np.random.uniform(0,1))
                print(f'retry at {_}')
                get_tv(_)

            else :
                print('else', e)

    async def request_async(_) :
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, functools.partial(get_tv, _=_))

    async def main(symbol_list) :
        await asyncio.gather(*[ request_async(_) for _ in symbol_list ])
        print('Done')

    asyncio.run(main(stock_list))

    """ Recheck Pulling Result """
    while True :
        none_list = []
        for _ in stock_list :
            # if isinstance(re_data[_], str) :
            #     none_list.append(_)

            if re_data[_] is None :
                none_list.append(_)

        if len(none_list) == 0 :
            break

        else :
            print('retrying none..', none_list)
            asyncio.run(main(none_list))

    return re_data

if __name__ == '__main__' :
    # stock_list = ['ADVANC', 'PTT', 'AOT', 'AP', 'JAS', 'JASIF', 'BTS', 'TRUE', 'GULF']
    stock_df = pd.read_csv('data/set50_stock_list.csv')
    stock_list = list(stock_df['symbol'])
    s = time.perf_counter()
    data = tv_async(stock_list)
    elapsed = time.perf_counter() - s
    print(data)
    print(len(data))
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')
