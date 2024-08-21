from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(n-1):
            if(prices[i]<prices[i+1]):
                profit += abs(prices[i]-prices[i+1])
            
        return profit

object = Solution()
print(object.maxProfit([7,1,5,3,6,4]))  # Output