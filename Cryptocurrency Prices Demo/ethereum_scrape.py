import requests
from bs4 import BeautifulSoup


#Ethereum

ethereum_url = "https://www.coindesk.com/price/ethereum" #URL for Ethereum Data that needs to be scraped
page = requests.get(ethereum_url)

ethereum_soup = BeautifulSoup(page.content, 'html.parser')

ethereum_price_raw = ethereum_soup.find('div', attrs={'class' : 'price-large'}) #Ethereum Price
ethereum_price = ethereum_price_raw.text.replace('', '')

ethereum_market_cap_raw = ethereum_soup.find('div', attrs={'class' : 'price-medium'}) #Ethereum Market Cap
ethereum_market_cap = ethereum_market_cap_raw.text.replace('', '')

ethereum_all_time_high_raw = ethereum_soup.find('div', attrs={'class' : 'price-small'}) #Ethereum All Time High
ethereum_all_time_high = ethereum_all_time_high_raw.text.replace('', '')

ethereum_percent_value_raw = ethereum_soup.find('span', attrs={'class' : 'percent-value-text'}) #Ethereum 24 Hour % change
ethereum_percent_value = ethereum_percent_value_raw.text.replace('', '')

ethereum_net_change_raw = ethereum_soup.find('div', attrs={'class' : 'price-change-medium'}) #Ethereum Net change
ethereum_net_change = ethereum_net_change_raw.text.replace('', '')
