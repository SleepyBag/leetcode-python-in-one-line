class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return (lambda nums, nums_copy: [nums.clear(), len([nums.append(i) for i in nums_copy if i != val])][1])(nums, nums.copy())