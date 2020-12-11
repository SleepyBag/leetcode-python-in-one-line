class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) if needle in haystack else -1