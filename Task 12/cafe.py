#define list of menu items
menu = ['Tea', 'Hot Chocolate', 'Coffee', 'Cookie']
#define dictionary of stock and price of menu items
stock = {'Tea':20, 'Hot Chocolate':15, 'Coffee':10, 'Cookie':7}
price = {'Tea':3.50, 'Hot Chocolate':3.00, 'Coffee':3.25, 'Cookie':2.00}

#initialise the total stock value as 0
total_stock = 0
#for loop for all the items in cafe menu
for items in menu:
  #multiply amount of stock by price to find value of that item's stock and define as item_value
  item_value = (stock[items] * price[items])
  #add each item's stock value to total_stock
  total_stock += item_value

#print total stock value to 2 decimal places for currency
print(f"The total value of the stock in the cafe is: ${total_stock:.2f}")