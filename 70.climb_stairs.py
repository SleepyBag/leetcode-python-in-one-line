class Solution:
    def climbStairs(self, n: int) -> int:
        return round(math.sqrt(5) / 5 * (((1 + math.sqrt(5)) / 2) ** (n + 1) - ((1 - math.sqrt(5)) / 2) ** (n + 1)))