class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')':'(', '}':'{', ']':'['}
        stack = []

        for p in s:
            if p in parentheses_map:
                if stack and stack[-1] == parentheses_map[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        if stack:
            return False
        else:
            return True


