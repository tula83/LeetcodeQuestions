#stock_buy_sell
def stock_buy_sell(arr):
    n=len(arr)
    min_price=9999
    profit=-9999
    for i in range(n):
        min_price=min(min_price,arr[i])
        profit=max(profit,arr[i]-min_price)
    return profit


print(stock_buy_sell([7,12,2,3,4,5,9]))
