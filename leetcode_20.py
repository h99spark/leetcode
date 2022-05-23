class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'[': ']', '{': '}', '(': ')'}
        stack = []

        for c in s:
            if c in paren:
                stack.append(c)
            elif (not stack) or (c != paren[stack.pop()]):
                return False

        return (stack == [])
