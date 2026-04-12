class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagrams_s = {}
        anagrams_t = {}

        for chars in s:
            if chars in anagrams_s:
                anagrams_s[chars] = anagrams_s[chars] + 1
            else:
                anagrams_s[chars] = 1

        for chars in t:
            if chars in anagrams_t:
                anagrams_t[chars] = anagrams_t[chars] + 1
            else:
                anagrams_t[chars] = 1

        return anagrams_t == anagrams_s
        