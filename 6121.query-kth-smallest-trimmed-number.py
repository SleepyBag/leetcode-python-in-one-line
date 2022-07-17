class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        return [sorted(list(map(lambda s: (int(s[1][-trim:]), s[0]), enumerate(nums))))[k - 1][1] for k, trim in queries]
