class Solution:
    def romanToInt(self, s: str) -> int:
        return sum({'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}[c] for c in s) + sum(collections.defaultdict(lambda: 0, {'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200})[c1 + c2] for c1, c2 in zip(s, s[1:]))
