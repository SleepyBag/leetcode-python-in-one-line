class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return (lambda nums, s: [[i, s[target - n]] for i, n in enumerate(nums) if target - n in s][0])(nums, {n: i for i, n in enumerate(nums)})