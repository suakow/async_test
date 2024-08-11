# Asynchronous Test Result

## Local Test

Computer spec : Macbook Pro (2020, Intel) 2 GHz Quad-Core Intel Core i5 (8 cores)

Bad internet connection

Baseline: 107.50 s

1. aync_asyncio : 29.91 s
2. async_asyncio2 : 32.88 s
3. async_pool : 28.90 s
4. async_joblib : 32.49 s
5. async_aiopool : 34.69 s

## Cloud Test

Computer spec : Digital Ocean 2 CPU cores

Baseline: 25.14

1. aync_asyncio : 25.69 s
2. async_asyncio2 : 27.68 s
3. async_pool : 62.21 s
4. async_joblib : 31.14 s
5. async_aiopool : 27.17