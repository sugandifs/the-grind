class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}

        for n in nums:
            if n in duplicates:
                return True
            else:
                duplicates[n] = 1

        return False
        