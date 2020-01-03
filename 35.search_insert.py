class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return [i for i, n in enumerate(nums + [target]) if n >= target][0]