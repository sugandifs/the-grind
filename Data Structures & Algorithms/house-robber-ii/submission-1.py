class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        if len(nums) == 1:
            return nums[0]
        
        if not nums:
            return 0

        prev1, prev2 = 0, 0
        rob1, rob2 = 0, 0

        for i in range(1, len(nums)):
            temp = max(nums[i] + prev1, prev2)

            prev1 = prev2
            prev2 = temp
        
        for i in range(0, len(nums) - 1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return max(prev2, rob2)