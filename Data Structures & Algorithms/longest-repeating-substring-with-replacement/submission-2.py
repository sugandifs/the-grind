class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        res = 0

        for c in chars:
            l = 0
            replacements = 0

            for r in range(len(s)):
                if s[r] != c:
                    replacements += 1

                while replacements > k:
                    if s[l] != c:
                        replacements -= 1
                    l += 1

                res = max(res, r - l + 1)

        return res
            
                


