class Solution:
    def reverse(self, x: int) -> int:
        return (lambda n: n if -(1<<31) <= n <= (1<<31) - 1 else 0)(int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1]))