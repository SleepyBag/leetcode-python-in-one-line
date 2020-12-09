class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce((lambda a, b: a ^ b), nums)
