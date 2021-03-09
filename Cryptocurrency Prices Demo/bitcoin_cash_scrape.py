import requests
from bs4 import BeautifulSoup


#Bitcoin Cash

bitcoin_cash_url = "https://www.coindesk.com/price/bitcoin-cash" #URL for Bitcoin Cash Data that needs to be scraped
page = requests.get(bitcoin_cash_url)

bitcoin_cash_soup = BeautifulSoup(page.content, 'html.parser')

bitcoin_cash_price_raw = bitcoin_cash_soup.find('div', attrs={'class' : 'price-large'}) #Bitcoin Cash Price
bitcoin_cash_price = bitcoin_cash_price_raw.text.replace('', '')

bitcoin_cash_market_cap_raw = bitcoin_cash_soup.find('div', attrs={'class' : 'price-medium'}) #Bitcoin Cash Market Cap
bitcoin_cash_market_cap = bitcoin_cash_market_cap_raw.text.replace('', '')

bitcoin_cash_all_time_high_raw = bitcoin_cash_soup.find('div', attrs={'class' : 'price-small'}) #Bitcoin Cash All Time High
bitcoin_cash_all_time_high = bitcoin_cash_all_time_high_raw.text.replace('', '')

bitcoin_cash_percent_value_raw = bitcoin_cash_soup.find('span', attrs={'class' : 'percent-value-text'}) #Bitcoin Cash 24 Hour % change
bitcoin_cash_percent_value = bitcoin_cash_percent_value_raw.text.replace('', '')

bitcoin_cash_net_change_raw = bitcoin_cash_soup.find('div', attrs={'class' : 'price-change-medium'}) #Bitcoin Cash Net change
bitcoin_cash_net_change = bitcoin_cash_net_change_raw.text.replace('', '')
