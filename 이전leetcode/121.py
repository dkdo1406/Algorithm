"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Input: prices = [7,1,5,3,6,4]
Output: 5
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# 앞에서부터 작은값을 저장한 후 오른쪽으로 가면서 저장한값보다 큰값 빼면됨
"""
import sys

prices = [4,2,1]
min_price = sys.maxsize
profit=0
for price in prices:
    min_price = min(min_price,price)
    profit = max(profit,price-min_price)
print(profit)