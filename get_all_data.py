import bs4 as bs
import pickle
import requests
import tushare as ts
import os

ts.set_token('3c1c9759637ce1480c6a5c7e7c1ee17e2cfb855f391d23122c8a1a0f')
pro = ts.pro_api()
# df = pro.daily(ts_code = '000001.SZ',start_date='20180101',end_date='20181118')
# print(df)

# # History CSI 300
# def find_and_save_CSI_300():
#     response = requests.get('https://en.wikipedia.org/wiki/CSI_300_Index')
#     soup = bs.BeautifulSoup(response.text, 'lxml')
#     table = soup.find('table', {'class':'wikitable sortable'})
#     tickers = []
#     for row in table.findAll('tr')[1:]:
#         ticker = row.findAll('td')[0].text
#         ticker = ticker[:6]
#         tickers.append(ticker)
        
#     with open('CSI_tickers.pickle', 'web') as f:
#         pickle.dump(tickers, f)
#     print(tickers)
#     return tickers


# find_and_save_CSI_300()

# Latest CSI 300
def find_and_save_CSI_300():
    CSI_300_df = ts.get_hs300s()
    print(CSI_300_df)
    
find_and_save_CSI_300()