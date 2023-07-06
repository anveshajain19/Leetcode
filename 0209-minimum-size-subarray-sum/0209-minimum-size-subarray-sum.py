class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        start = 0
        min_length = float("inf")

        for i, num in enumerate(nums):
            current_sum += num

            while current_sum >= target:
                min_length = min(min_length, i - start + 1)
                current_sum -= nums[start]
                start += 1

        if min_length == float("inf"):
            return 0

        return min_length