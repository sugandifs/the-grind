class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = defaultdict(int)
        result = 0

        for num in nums:
            if not map[num]:
                map[num] = map[num - 1] + map[num + 1 ] + 1
                map[num - map[num-1]] = map[num]
                map[num + map[num+1]] = map[num]
                result = max(result, map[num])

        return result