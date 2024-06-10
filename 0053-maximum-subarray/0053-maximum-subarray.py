class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        ans = 0
        for i in range(len(nums)):
            ans += nums[i] 
            if ans > maxSum:
                maxSum = ans
            if ans < 0:
                ans = 0
        return maxSum