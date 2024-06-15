class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        a = -1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                a = nums[i]
                break
        return a