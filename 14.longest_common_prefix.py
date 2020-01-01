class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return (lambda f, *args: f(f, *args))(lambda f, strs: strs[0] if len(strs) == 1 else f(f, strs[: -2] + [strs[-1][: [a == b for a, b in zip(strs[-1] + '&', strs[-2] + '#')].index(False)]]), strs) if strs else ""