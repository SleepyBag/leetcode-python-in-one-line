class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(splited[-1]) if (splited := s.split()) else 0