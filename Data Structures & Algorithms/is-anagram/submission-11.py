class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_anagram = {}
        t_anagram = {}

        for letter in t:
            if letter in t_anagram:
                t_anagram[letter] += 1
            else:
                t_anagram[letter] = 1

        print(t_anagram)

        for letter in s:
            if letter in s_anagram:
                s_anagram[letter] += 1
            else:
                s_anagram[letter] = 1

        print(s_anagram)

        for letter, freq in s_anagram.items():
            if letter not in t_anagram or t_anagram[letter] != freq:
                return False

        return True

        