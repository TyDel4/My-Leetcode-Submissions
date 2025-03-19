class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp_array = []
        biggest_difference = 0

        for i in range(len(prices)):
            temp_array = prices[i:]
            if (max(temp_array) - prices[i] > biggest_difference):
                biggest_difference = max(temp_array) - prices[i]
        return biggest_difference
    