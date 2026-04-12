class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        window = set()
        max_size = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            curr_size = r - l + 1
            max_size = max(curr_size, max_size)

        return max_size
