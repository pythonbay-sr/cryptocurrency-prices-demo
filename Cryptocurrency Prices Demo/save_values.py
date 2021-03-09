import xlwt
from xlwt import Workbook
from bitcoin_scrape import *
from ethereum_scrape import *
from litecoin_scrape import *
from monero_scrape import *
from bitcoin_cash_scrape import *


def save():    
    #Create a Workbook
    wb = Workbook()
    
    #Create a Excel Spreadsheet
    cp_values_sheet = wb.add_sheet('Cryptocurrency Values')


    #Save Bitcoin Values

    cp_values_sheet.write(2, 0, 'Bitcoin')
    cp_values_sheet.write(2, 2, bitcoin_price)
    cp_values_sheet.write(2, 4, bitcoin_market_cap)
    cp_values_sheet.write(2, 6, bitcoin_all_time_high)
    cp_values_sheet.write(2, 8, bitcoin_percent_value)
    cp_values_sheet.write(2, 10, bitcoin_net_change)


    #Save Ethereum Values

    cp_values_sheet.write(3, 0, 'Ethereum')
    cp_values_sheet.write(3, 2, ethereum_price)
    cp_values_sheet.write(3, 4, ethereum_market_cap)
    cp_values_sheet.write(3, 6, ethereum_all_time_high)
    cp_values_sheet.write(3, 8, ethereum_percent_value)
    cp_values_sheet.write(3, 10, ethereum_net_change)


    #Save Litecoin Values

    cp_values_sheet.write(4, 0, 'Litecoin')
    cp_values_sheet.write(4, 2, litecoin_price)
    cp_values_sheet.write(4, 4, litecoin_market_cap)
    cp_values_sheet.write(4, 6, litecoin_all_time_high)
    cp_values_sheet.write(4, 8, litecoin_percent_value)
    cp_values_sheet.write(4, 10, litecoin_net_change)


    #Save Monero Values

    cp_values_sheet.write(5, 0, 'Monero')
    cp_values_sheet.write(5, 2, monero_price)
    cp_values_sheet.write(5, 4, monero_market_cap)
    cp_values_sheet.write(5, 6, monero_all_time_high)
    cp_values_sheet.write(5, 8, monero_percent_value)
    cp_values_sheet.write(5, 10, monero_net_change)


    #Save Monero Values

    cp_values_sheet.write(6, 0, 'BTC Cash')
    cp_values_sheet.write(6, 2, bitcoin_cash_price)
    cp_values_sheet.write(6, 4, bitcoin_cash_market_cap)
    cp_values_sheet.write(6, 6, bitcoin_cash_all_time_high)
    cp_values_sheet.write(6, 8, bitcoin_cash_percent_value)
    cp_values_sheet.write(6, 10, bitcoin_cash_net_change)


    wb.save('cryptocurrency_values.xls')
