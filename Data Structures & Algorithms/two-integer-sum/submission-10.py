class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n

            if diff in indices:
                return [indices[diff], i]
            else:
                indices[n] = i

        return
             