class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            key = {}
            for letter in string:
                if letter in key:
                    key[letter] += 1
                else:
                    key[letter] = 1

            key_tuple = tuple(sorted(key.items()))

            if key_tuple in groups:
                groups[key_tuple].append(string)
            else:
                groups[key_tuple] = [string]

        return list(groups.values())



