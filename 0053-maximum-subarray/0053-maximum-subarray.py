class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        var = float('-inf')
        count = 0
        for num in nums:
            count = max(num, count+ num)
            var = max(var, count)
        return var
        