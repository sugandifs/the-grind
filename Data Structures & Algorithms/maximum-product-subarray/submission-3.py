class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ending = min_ending = result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_ending, min_ending = min_ending, max_ending
            
            max_ending = max(nums[i], max_ending * nums[i])
            min_ending = min(nums[i], min_ending * nums[i])

            result = max(result, max_ending)

        return result
