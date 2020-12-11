class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return (lambda nums, unique_nums: [nums.clear(), len([nums.append(i) for i in unique_nums])][1])(nums, sorted(list(set(nums))))
