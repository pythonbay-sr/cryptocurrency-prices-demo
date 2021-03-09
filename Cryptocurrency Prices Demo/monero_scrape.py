import requests
from bs4 import BeautifulSoup


#Monero

monero_url = "https://www.coindesk.com/price/monero" #URL for Monero Data that needs to be scraped
page = requests.get(monero_url)

monero_soup = BeautifulSoup(page.content, 'html.parser')

monero_price_raw = monero_soup.find('div', attrs={'class' : 'price-large'}) #Monero Price
monero_price = monero_price_raw.text.replace('', '')

monero_market_cap_raw = monero_soup.find('div', attrs={'class' : 'price-medium'}) #Monero Market Cap
monero_market_cap = monero_market_cap_raw.text.replace('', '')

monero_all_time_high_raw = monero_soup.find('div', attrs={'class' : 'price-small'}) #Monero All Time High
monero_all_time_high = monero_all_time_high_raw.text.replace('', '')

monero_percent_value_raw = monero_soup.find('span', attrs={'class' : 'percent-value-text'}) #Monero 24 Hour % change
monero_percent_value = monero_percent_value_raw.text.replace('', '')

monero_net_change_raw = monero_soup.find('div', attrs={'class' : 'price-change-medium'}) #Monero Net change
monero_net_change = monero_net_change_raw.text.replace('', '')
