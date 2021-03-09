import requests
from bs4 import BeautifulSoup
import urllib.request


#Bitcoin

bitcoin_url = "https://www.coindesk.com/price/bitcoin" #URL for Bitcoin Data that needs to be scraped
page = requests.get(bitcoin_url)

bitcoin_soup = BeautifulSoup(page.content, 'html.parser')

bitcoin_price_raw = bitcoin_soup.find('div', attrs={'class' : 'price-large'}) #Bitcoin Price
bitcoin_price = bitcoin_price_raw.text.replace('', '')

bitcoin_market_cap_raw = bitcoin_soup.find('div', attrs={'class' : 'price-medium'}) #Bitcoin Market Cap
bitcoin_market_cap = bitcoin_market_cap_raw.text.replace('', '')

bitcoin_all_time_high_raw = bitcoin_soup.find('div', attrs={'class' : 'price-small'}) #Bitcoin All Time High
bitcoin_all_time_high = bitcoin_all_time_high_raw.text.replace('', '')

bitcoin_percent_value_raw = bitcoin_soup.find('span', attrs={'class' : 'percent-value-text'}) #Bitcoin 24 Hour % change
bitcoin_percent_value = bitcoin_percent_value_raw.text.replace('', '')

bitcoin_net_change_raw = bitcoin_soup.find('div', attrs={'class' : 'price-change-medium'}) #Bitcoin Net change
bitcoin_net_change = bitcoin_net_change_raw.text.replace('', '')


#Download Bitcoin Graph

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + ".png"
    urllib.request.urlretrieve(url, full_path)

url = "https://bitcoincharts.com/charts/chart.png?width=940&m=bitstampUSD&SubmitButton=Draw&r=60&i=&c=0&s=&e=&Prev=&Next=&t=S&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=1&cv=0&ps=0&l=0&p=0&"
file_name = "bitcoin"

dl_jpg(url, r'C:\\Users\\Nikola Kostic\\Desktop\\', file_name)
