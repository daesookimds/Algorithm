import sys
from typing import List

def maxProfit_brute_force(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

def maxProfit_Kadanes(prices: List[int]) -> int:
    max_profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


def test_case():
    case1 = [7, 1, 5, 3, 6, 4]

    result1 = maxProfit_brute_force(case1)
    print(result1)

    result2 = maxProfit_Kadanes(case1)
    print(result2)