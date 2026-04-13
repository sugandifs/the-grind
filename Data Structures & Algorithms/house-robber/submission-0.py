class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for house in range(2, len(nums)):
            dp[house] = max(dp[house- 1], nums[house] + dp[house-2])
        
        return dp[-1]