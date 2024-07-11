# Solution 2,
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if (prices[i] - min > maxProfit):
                maxProfit = prices[i] - min
            if prices[i] < min:
                min = prices[i]




# Solution 1, worst case O(n2)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # create a maxProfit var
#         maxProfit = 0
#         maxVal = max(prices)
#         # iterate through and find the max in the following days
#         for i in range(len(prices) - 1):
#             # continue if the max potential profit for this value is not over maxProfit
#             thisProfit = maxVal - prices[i]
#             if (thisProfit > maxProfit):
#                 maxProfit = thisProfit
#             elif(thisProfit == 0):
#                 maxVal = max(prices[i+1:])
#             if (maxVal <= maxProfit):
#                     return maxProfit
#         return maxProfit