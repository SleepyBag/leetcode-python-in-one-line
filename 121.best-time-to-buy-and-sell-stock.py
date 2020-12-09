class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return 0 if not prices else (bottom := inf, max(p - (bottom := min(bottom, p)) for p in prices))[-1]
