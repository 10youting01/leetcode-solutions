class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = 101
        max_pro = 0
        for p in prices:
            if p < curr_min: 
                curr_min = p
            if (p - curr_min) > max_pro:
                max_pro = p - curr_min
        return max_pro