import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from save_values import *
from bitcoin_scrape import *
from ethereum_scrape import *
from litecoin_scrape import *
from monero_scrape import *
from bitcoin_cash_scrape import *
import time


#Set up the Program

root = tkinter.Tk()
root.title("Cryptocurrency Prices")
root.geometry("1200x910")
#root.resizable(width=False, height=False)
root.configure(bg="#2b2a27")
root.iconbitmap('logo.ico')


#Close the Main Window

def close_window():
    response = messagebox.askquestion("Exit the Program", "Do you really want to exit the program?")
    if response == 'yes':
        root.destroy()
    else:
        pass


#Help Window

def help():
    help_root = tkinter.Tk()
    help_root.title("Help")
    help_root.geometry("670x250")
    help_root.resizable(width=False, height=False)
    help_root.configure(bg="#2b2a27")
    help_root.iconbitmap('logo.ico')

    Help_Title = Label(help_root, text="Help", font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
    Help_Title.place(x=300, y=30)

    Help_Text = Label(help_root, text="If you have any questions about the software \n or you found a bug, please contact : \n nikosta350@gmail.com", font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
    Help_Text.place(x=30, y=80)


#Menubar

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=close_window)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=help)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


#Labels

Price_Text = Label(root, text="Price : ", font=("Century Gothic", 15), fg="#fff", bg="#2b2a27")
Price_Text.place(x=200, y=70)

Market_Cap_Text = Label(root, text="Market Cap : ", font=("Century Gothic", 15), fg="#fff", bg="#2b2a27")
Market_Cap_Text.place(x=370, y=70)

All_Time_High_Text = Label(root, text="All Time High : ", font=("Century Gothic", 15), fg="#fff", bg="#2b2a27")
All_Time_High_Text.place(x=540, y=70)

Percent_Value_Text = Label(root, text="24 Hour change : ", font=("Century Gothic", 15), fg="#fff", bg="#2b2a27")
Percent_Value_Text.place(x=710, y=70)

Net_change_Text = Label(root, text="Net change : ", font=("Century Gothic", 15), fg="#fff", bg="#2b2a27")
Net_change_Text.place(x=900, y=70)


#Bitcoin

Bitcoin_Label = Label(root, text="Bitcoin", font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Label.place(x=50, y=130)

Bitcoin_Price = Label(root, text=bitcoin_price, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Price.place(x=200, y=130)

Bitcoin_Market_Cap = Label(root, text=bitcoin_market_cap, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Market_Cap.place(x=370, y=130)

Bitcoin_All_Time_High = Label(root, text=bitcoin_all_time_high, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_All_Time_High.place(x=540, y=130)

if float(bitcoin_percent_value) > 0:
    Bitcoin_Percent_Value = Label(root, text=(str(bitcoin_percent_value) + "%"), font=("Century Gothic", 20), fg="#20c950", bg="#2b2a27")
    Bitcoin_Percent_Value.place(x=710, y=130)
else:
    Bitcoin_Percent_Value = Label(root, text=(str(bitcoin_percent_value) + "%"), font=("Century Gothic", 20), fg="#c92e20", bg="#2b2a27")
    Bitcoin_Percent_Value.place(x=710, y=130)

Bitcoin_Net_change = Label(root, text=bitcoin_net_change, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Net_change.place(x=900, y=130)

#Bitcoin Graph Label

Bitcoin_Graph_Label = Label(root, text="Bitcoin Graphic", font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Graph_Label.place(x=490, y=450)

#Bitcoin Graph

time.sleep(2)
img_full_raw = Image.open("bitcoin.png")
img_raw = img_full_raw.resize((800, 350), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img_raw)
panel = Label(root, image = img, relief=FLAT)
panel.place(x=190, y=510)


#Ethereum

Ethereum_Label = Label(root, text="Ethereum", font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Ethereum_Label.place(x=50, y=190)

Ethereum_Price = Label(root, text=ethereum_price, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Ethereum_Price.place(x=200, y=190)

Ethereum_Market_Cap = Label(root, text=ethereum_market_cap, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Ethereum_Market_Cap.place(x=370, y=190)

Ethereum_All_Time_High = Label(root, text=ethereum_all_time_high, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Ethereum_All_Time_High.place(x=540, y=190)

if float(ethereum_percent_value) > 0:
    Ethereum_Percent_Value = Label(root, text=(str(ethereum_percent_value) + "%"), font=("Century Gothic", 20), fg="#20c950", bg="#2b2a27")
    Ethereum_Percent_Value.place(x=710, y=190)
else:
    Ethereum_Percent_Value = Label(root, text=(str(ethereum_percent_value) + "%"), font=("Century Gothic", 20), fg="#c92e20", bg="#2b2a27")
    Ethereum_Percent_Value.place(x=710, y=190)

Ethereum_Net_change = Label(root, text=ethereum_net_change, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Ethereum_Net_change.place(x=900, y=190)


#Litecoin

Litecoin_Label = Label(root, text="Litecoin", font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Litecoin_Label.place(x=50, y=250)

Litecoin_Price = Label(root, text=litecoin_price, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Litecoin_Price.place(x=200, y=250)

Litecoin_Market_Cap = Label(root, text=litecoin_market_cap, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Litecoin_Market_Cap.place(x=370, y=250)

Litecoin_All_Time_High = Label(root, text=litecoin_all_time_high, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Litecoin_All_Time_High.place(x=540, y=250)

if float(litecoin_percent_value) > 0:
    Litecoin_Percent_Value = Label(root, text=(str(litecoin_percent_value) + "%"), font=("Century Gothic", 20), fg="#20c950", bg="#2b2a27")
    Litecoin_Percent_Value.place(x=710, y=250)
else:
    Litecoin_Percent_Value = Label(root, text=(str(litecoin_percent_value) + "%"), font=("Century Gothic", 20), fg="#c92e20", bg="#2b2a27")
    Litecoin_Percent_Value.place(x=710, y=250)

Litecoin_Net_change = Label(root, text=litecoin_net_change, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Litecoin_Net_change.place(x=900, y=250)


#Monero

Monero_Label = Label(root, text="Monero", font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Monero_Label.place(x=50, y=310)

Monero_Price = Label(root, text=monero_price, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Monero_Price.place(x=200, y=310)

Monero_Market_Cap = Label(root, text=monero_market_cap, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Monero_Market_Cap.place(x=370, y=310)

Monero_All_Time_High = Label(root, text=monero_all_time_high, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Monero_All_Time_High.place(x=540, y=310)

if float(monero_percent_value) > 0:
    Monero_Percent_Value = Label(root, text=(str(monero_percent_value) + "%"), font=("Century Gothic", 20), fg="#20c950", bg="#2b2a27")
    Monero_Percent_Value.place(x=710, y=310)
else:
    Monero_Percent_Value = Label(root, text=(str(monero_percent_value) + "%"), font=("Century Gothic", 20), fg="#c92e20", bg="#2b2a27")
    Monero_Percent_Value.place(x=710, y=310)

Monero_Net_change = Label(root, text=monero_net_change, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Monero_Net_change.place(x=900, y=310)


#Bitcoin Cash

Bitcoin_Cash_Label = Label(root, text="BTC Cash", font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Cash_Label.place(x=50, y=370)

Bitcoin_Cash_Price = Label(root, text=bitcoin_cash_price, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Cash_Price.place(x=200, y=370)

Bitcoin_Cash_Market_Cap = Label(root, text=bitcoin_cash_market_cap, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Cash_Market_Cap.place(x=370, y=370)

Bitcoin_Cash_All_Time_High = Label(root, text=bitcoin_cash_all_time_high, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Cash_All_Time_High.place(x=540, y=370)

if float(bitcoin_cash_percent_value) > 0:
    Bitcoin_Cash_Percent_Value = Label(root, text=(str(bitcoin_cash_percent_value) + "%"), font=("Century Gothic", 20), fg="#20c950", bg="#2b2a27")
    Bitcoin_Cash_Percent_Value.place(x=710, y=370)
else:
    Bitcoin_Cash_Percent_Value = Label(root, text=(str(bitcoin_cash_percent_value) + "%"), font=("Century Gothic", 20), fg="#c92e20", bg="#2b2a27")
    Bitcoin_Cash_Percent_Value.place(x=710, y=370)

Bitcoin_Cash_Net_change = Label(root, text=bitcoin_cash_net_change, font=("Century Gothic", 20), fg="#fff", bg="#2b2a27")
Bitcoin_Cash_Net_change.place(x=900, y=370)


#Root Mainloop

root.mainloop()
