class Solution:
    def isValid(self, s: str) -> bool:
        return (lambda f, *args: f(f, *args))(lambda f, stack, s:(f(f, stack + [s[0]], s[1:]) if s[0] in ['{', '[', '('] else (False if not stack else (f(f, stack[: -1], s[1:]) if s[0] == ']' and stack[-1] == '[' or s[0] == ')' and stack[-1] == '(' or s[0] == '}' and stack[-1] == '{' else False))) if s else not stack, [], s)