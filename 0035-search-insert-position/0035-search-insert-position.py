class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
           
        nums.append(target)
        a = sorted(nums)
        if target in a:
            return a.index(target)
                