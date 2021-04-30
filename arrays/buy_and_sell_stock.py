"""
Given an array of numbers consisting of daily stock prices, 
calculate the maximum amount of profit that can be made from buying on one day and 
selling on another.

In an array of prices, each index represents a day, 
and the value on that index represents the price of the stocks on that day.
Profit = Selling Price - Buying Price

A = [310,315,275,295,260,270,290,230,255,250]
max profit  = 30
"""

def buy_and_sell_stock(prices):
    
    length_of_prices = len(prices)
    

    if length_of_prices > 1:
        l = prices[0]
        h = prices[0]
        m = 0
        new_max = 0
        for i in range(1,length_of_prices):
            if prices[i]>h:
                new_max = prices[i]-h 
                h = prices[i]

            if prices[i]>l:
                new_max = prices[i]-l
            else:
                l = prices[i]

            if new_max > m :
                m = new_max
      
        return m
    else:
        return A[0]
    


        

A = [310,315,275,295,260,270,290,230,255,250]
print(buy_and_sell_stock(A))
