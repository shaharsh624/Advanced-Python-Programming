import logging
from tkinter import *

logging.basicConfig(filename="std.log", format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

company_price = {
    "RELIANCE": 2500,
    "TCS": 3500,
    "HDFCBANK": 1200,
    "INFY": 1500,
    "ICICIBANK": 800,
    "HCLTECH": 1200,
    "KOTAKBANK": 1800,
    "HINDUNILVR": 2200,
    "BAJFINANCE": 4500,
    "ITC": 200
}
companies = list(company_price.keys())


def selected_stock(self):
    stock = selected_var.get()
    label_price.config(text=f"${company_price[stock]}")
    return stock
def buy_stock():
    stock = selected_var.get()
    quantity = quantity_counter.get()
    price = company_price[stock]
    print(f"Bought {quantity} shares of {stock} at {price}")
    logger.info(f"Bought {quantity} shares of {stock} at {price}")
def sell_stock():
    stock = selected_var.get()
    quantity = quantity_counter.get()
    price = company_price[stock]
    print(f"Sold {quantity} shares of {stock} at {price}")
    logger.info(f"Sold {quantity} shares of {stock} at {price}")

win = Tk()
win.title("Tkinter Program")
win.minsize(width=270, height=400)

selected_var = StringVar()
selected_var.set("Select Any Stock")

label_stock = OptionMenu(win, selected_var, *companies, command=selected_stock)
label_stock.grid(row=0, column=0, columnspan=2, pady=(20, 5))

label_price = Label(text="$0", font=('Roboto', 14, 'bold'))
label_price.grid(row=1, column=0, columnspan=2, pady=(0, 20))

quantity_label = Label(win, text="Quantity:", font=15)
quantity_label.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

quantity_counter = Spinbox(from_=1, to=100, width=10, font=14, )
quantity_counter.grid(row=3, column=0, padx=10, pady=5, columnspan=2, rowspan=2)

button_buy = Button(text="Buy", command=buy_stock, bg="#4CAF50", fg="white", width=10, font=10)
button_buy.grid(row=5, column=0, padx=5, pady=20)

button_sell = Button(text="Sell", command=sell_stock, bg="#FF5733", fg="white", width=10, font=10)
button_sell.grid(row=5, column=1, padx=5, pady=20)

win.mainloop()
