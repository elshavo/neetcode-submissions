class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two Pointers
        l, r = 0, 1 #left= buy, right=sell
        maxp = 0 #maximum profit

        while r < len(prices): # recorrer r desde el dia 0 hasta ultimo dia.
            #profit?
            if prices[l] < prices[r]: #l needs to be less to have profit 
                profit = prices[r] - prices[l] #calculate profit
                maxp = max(maxp, profit) #takes the highest one
            #no profit
            else:
                l = r #change day to the r because is the lowest 
            
            r = r + 1 #move to next day
        return maxp #returns max profit











        




"""
        #Two Pointers
        l, r = 0, 1 #left= buy, right=sell
        maxp = 0 #maximum profit

        while r < len(prices): # recorrer r desde el dia 0 hasta ultimo dia.
            #profit?
            if prices[l] < prices[r]: #l needs to be less to have profit 
                profit = prices[r] - prices[l] #calculate profit
                maxp = max(maxp, profit) #takes the highest one
            #no profit
            else:
                l = r #change day to the r because is the lowest 
            
            r = r + 1 #move to next day
        return maxp #returns max profit
"""













"""
        l, cur, best = -1, 0, 0
        for r in range(len(prices)): #starts -1,0 len of prices
            cur = cur + prices[r] #adds the value of prices to cur
            while cur >= prices: #
                l = l + 1
                cur = cur - prices[l]
            best = max(best, r - 1)

#inicie a comprar desde dia 1 #diacompra = prices[0]
#se hace simulacion de profit con dia siguiente profit = dia[1](venta) - dia[0](compra)
#si profit > best:
#best = best + profit





#si gasto no es 
        
"""