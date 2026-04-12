class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            length = len(string)
            result += str(length) + "#" + string

        return result

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1

            decoded_strs.append(s[i:i+length])
            i += length

        return decoded_strs

