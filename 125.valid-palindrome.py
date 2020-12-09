class Solution:
    def isPalindrome(self, s: str) -> bool:
        return [c for c in s.lower() if c.isalnum()] == [c for c in s.lower()[::-1] if c.isalnum()]
