class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}

        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1
        
        window = {}
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("inf")
        l = 0

        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1 < resLen):
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res

        if resLen != float('inf'):
            return s[l: r+1]
        else:
            return ""
