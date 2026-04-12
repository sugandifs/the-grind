class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # make an array of all zeroes
            for c in s:
                count[ord(c) - ord('a')] += 1
                # ord returns the unicode number, 
                # so that the difference places it into the
                # right index

            res[tuple(count)].append(s)
            # use the alphabet array as the key to the hashmap

        return list(res.values())

