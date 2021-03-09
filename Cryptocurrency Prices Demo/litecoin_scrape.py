import requests
from bs4 import BeautifulSoup


#Litecoin

litecoin_url = "https://www.coindesk.com/price/litecoin" #URL for Litecoin Data that needs to be scraped
page = requests.get(litecoin_url)

litecoin_soup = BeautifulSoup(page.content, 'html.parser')

litecoin_price_raw = litecoin_soup.find('div', attrs={'class' : 'price-large'}) #Litecoin Price
litecoin_price = litecoin_price_raw.text.replace('', '')

litecoin_market_cap_raw = litecoin_soup.find('div', attrs={'class' : 'price-medium'}) #Litecoin Market Cap
litecoin_market_cap = litecoin_market_cap_raw.text.replace('', '')

litecoin_all_time_high_raw = litecoin_soup.find('div', attrs={'class' : 'price-small'}) #Litecoin All Time High
litecoin_all_time_high = litecoin_all_time_high_raw.text.replace('', '')

litecoin_percent_value_raw = litecoin_soup.find('span', attrs={'class' : 'percent-value-text'}) #Litecoin 24 Hour % change
litecoin_percent_value = litecoin_percent_value_raw.text.replace('', '')

litecoin_net_change_raw = litecoin_soup.find('div', attrs={'class' : 'price-change-medium'}) #Litecoin Net change
litecoin_net_change = litecoin_net_change_raw.text.replace('', '')
